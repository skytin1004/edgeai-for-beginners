<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "94b65d49961cabc07f76062d09a5d09c",
  "translation_date": "2025-10-09T16:56:28+00:00",
  "source_file": "Workshop/Session06-ModelsAsTools.md",
  "language_code": "vi"
}
-->
# Buổi 6: Foundry Local – Mô hình như công cụ

## Tóm tắt

Xem các mô hình như những công cụ có thể kết hợp trong một lớp vận hành AI cục bộ. Buổi học này hướng dẫn cách liên kết nhiều cuộc gọi SLM/LLM chuyên biệt, định tuyến nhiệm vụ một cách chọn lọc, và cung cấp một giao diện SDK thống nhất cho các ứng dụng. Bạn sẽ xây dựng một bộ định tuyến mô hình nhẹ + trình lập kế hoạch nhiệm vụ, tích hợp nó vào một kịch bản ứng dụng, và phác thảo lộ trình mở rộng lên Azure AI Foundry cho khối lượng công việc sản xuất.

## Mục tiêu học tập

- **Hình dung** các mô hình như những công cụ nguyên tử với khả năng được khai báo
- **Định tuyến** yêu cầu dựa trên ý định / điểm số theo phương pháp heuristic
- **Liên kết** đầu ra qua các nhiệm vụ nhiều bước (phân rã → giải quyết → tinh chỉnh)
- **Tích hợp** một API khách thống nhất cho các ứng dụng hạ nguồn
- **Mở rộng** thiết kế lên đám mây (hợp đồng tương thích OpenAI)

## Điều kiện tiên quyết

- Hoàn thành các buổi 1–5
- Nhiều mô hình cục bộ được lưu trữ (ví dụ: `phi-4-mini`, `deepseek-coder-1.3b`, `qwen2.5-0.5b`)

### Đoạn mã môi trường đa nền tảng

Windows PowerShell:
```powershell
py -m venv .venv
 .\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install foundry-local-sdk openai
```

macOS / Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

Truy cập dịch vụ từ xa/VM từ macOS:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## Quy trình demo (30 phút)

### 1. Khai báo khả năng công cụ (5 phút)

Tạo `samples/06-tools/models_catalog.py`:

```python
CATALOG = {
  "phi-4-mini": {
    "capabilities": ["general", "reasoning", "summarize"],
    "priority": 2
  },
  "deepseek-coder-1.3b": {
    "capabilities": ["code", "refactor", "explain_code"],
    "priority": 1
  },
  "qwen2.5-0.5b": {
    "capabilities": ["fast", "classification", "lightweight"],
    "priority": 3
  }
}
```


### 2. Phát hiện ý định & định tuyến (8 phút)

Tạo `samples/06-tools/router.py`:

```python
#!/usr/bin/env python3
"""Model-as-tool router using Foundry Local OpenAI-compatible endpoint."""
from openai import OpenAI
from models_catalog import CATALOG
import re

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

INTENT_RULES = [
  (re.compile(r"code|function|refactor|bug|optimi", re.I), "code"),
  (re.compile(r"summari|abstract|tl;dr", re.I), "summarize"),
  (re.compile(r"classif|label|category", re.I), "classification"),
]

def detect_intent(prompt: str) -> str:
    for pat, intent in INTENT_RULES:
        if pat.search(prompt):
            return intent
    return "general"

def select_model(intent: str) -> str:
    # Score catalog: capability match first, then priority
    scored = []
    for name, meta in CATALOG.items():
        caps = meta["capabilities"]
        match = intent in caps
        scored.append((name, match, meta["priority"]))
    # Sort: match True first, then lowest priority value
    scored.sort(key=lambda t: (not t[1], t[2]))
    return scored[0][0]

def run(prompt: str):
    intent = detect_intent(prompt)
    model = select_model(intent)
    resp = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=400,
        temperature=0.5
    )
    return {"intent": intent, "model": model, "output": resp.choices[0].message.content}

if __name__ == "__main__":
    tests = [
        "Refactor this Python function for readability",
        "Summarize the importance of local AI governance",
        "Classify this feedback: 'The UI is slow and confusing'"
    ]
    for t in tests:
        r = run(t)
        print(f"Prompt: {t}\nModel: {r['model']} (intent={r['intent']})\nOutput: {r['output'][:160]}...\n")
```


### 3. Liên kết nhiệm vụ nhiều bước (7 phút)

Tạo `samples/06-tools/pipeline.py`:

```python
#!/usr/bin/env python3
"""Multi-step pipeline: plan -> solve -> refine using specialized models."""
from openai import OpenAI
from router import detect_intent, select_model

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

def chat(model, content, temp=0.4):
    r = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": content}],
        max_tokens=350,
        temperature=temp
    )
    return r.choices[0].message.content

def pipeline(task: str):
    plan_model = select_model("general")
    plan = chat(plan_model, f"Break the task into 3 ordered steps. Task: {task}")
    steps = [s for s in plan.split('\n') if s.strip()][:3]
    outputs = []
    for step in steps:
        intent = detect_intent(step)
        model = select_model(intent)
        out = chat(model, step)
        outputs.append((step, model, out))
    refine_model = select_model("summarize")
    combined = '\n'.join(o[2] for o in outputs)
    refined = chat(refine_model, f"Condense results into a cohesive answer:\n{combined}")
    return {"plan": plan, "steps": outputs, "final": refined}

if __name__ == '__main__':
    result = pipeline("Generate a refactored version of a slow Python loop and summarize performance gains.")
    print("PLAN:\n", result['plan'])
    print("FINAL:\n", result['final'][:400])
```


### 4. Dự án khởi đầu: Điều chỉnh `06-models-as-tools` (5 phút)

Cải tiến:
- Thêm hỗ trợ token streaming (cập nhật giao diện người dùng theo tiến trình)
- Thêm điểm số độ tin cậy: sự trùng lặp từ vựng hoặc tiêu chí gợi ý
- Xuất JSON trace (ý định → mô hình → độ trễ → sử dụng token)
- Thực hiện tái sử dụng bộ nhớ cache cho các bước con lặp lại

### 5. Lộ trình mở rộng lên Azure (5 phút)

| Lớp | Cục bộ (Foundry) | Đám mây (Azure AI Foundry) | Chiến lược chuyển đổi |
|-----|------------------|---------------------------|-----------------------|
| Định tuyến | Python heuristic | Microservice bền vững | Đóng gói & triển khai API |
| Mô hình | SLMs được lưu trữ | Triển khai được quản lý | Ánh xạ tên cục bộ sang ID triển khai |
| Khả năng quan sát | Thống kê CLI/thủ công | Nhật ký & số liệu tập trung | Thêm sự kiện trace có cấu trúc |
| Bảo mật | Chỉ host cục bộ | Xác thực mạng Azure | Thêm key vault cho thông tin bí mật |
| Chi phí | Tài nguyên thiết bị | Thanh toán theo mức sử dụng | Thêm giới hạn ngân sách |

## Danh sách kiểm tra xác thực

```powershell
foundry model run phi-4-mini
foundry model run deepseek-coder-1.3b
python samples/06-tools/router.py
python samples/06-tools/pipeline.py
```

Đảm bảo lựa chọn mô hình dựa trên ý định và đầu ra cuối cùng được tinh chỉnh.

## Xử lý sự cố

| Vấn đề | Nguyên nhân | Cách khắc phục |
|--------|-------------|----------------|
| Tất cả nhiệm vụ được định tuyến đến cùng một mô hình | Quy tắc yếu | Làm phong phú tập regex INTENT_RULES |
| Pipeline thất bại giữa bước | Mô hình chưa được tải | Chạy `foundry model run <model>` |
| Đầu ra kém liên kết | Không có giai đoạn tinh chỉnh | Thêm bước tóm tắt/xác thực |

## Tài liệu tham khảo

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Tài liệu Azure AI Foundry: https://learn.microsoft.com/azure/ai-foundry
- Mẫu chất lượng gợi ý: Xem Buổi 2

---

**Thời lượng buổi học**: 30 phút  
**Độ khó**: Chuyên gia

## Kịch bản mẫu & ánh xạ workshop

| Kịch bản / Notebook workshop | Kịch bản | Mục tiêu | Nguồn dữ liệu / danh mục |
|------------------------------|----------|----------|--------------------------|
| `samples/session06/models_router.py` / `notebooks/session06_models_router.ipynb` | Trợ lý nhà phát triển xử lý các gợi ý ý định hỗn hợp (tái cấu trúc, tóm tắt, phân loại) | Ý định heuristic → định tuyến alias mô hình với sử dụng token | `CATALOG` nội tuyến + regex `RULES` |
| `samples/session06/models_pipeline.py` / `notebooks/session06_models_pipeline.ipynb` | Lập kế hoạch & tinh chỉnh nhiều bước cho nhiệm vụ hỗ trợ mã hóa phức tạp | Phân rã → thực thi chuyên biệt → bước tinh chỉnh tóm tắt | Cùng `CATALOG`; các bước được dẫn xuất từ đầu ra kế hoạch |

### Tường thuật kịch bản
Một công cụ tăng năng suất kỹ thuật nhận các nhiệm vụ không đồng nhất: tái cấu trúc mã, tóm tắt ghi chú kiến trúc, phân loại phản hồi. Để giảm độ trễ & sử dụng tài nguyên, một mô hình nhỏ tổng quát lập kế hoạch và tóm tắt, một mô hình chuyên về mã xử lý tái cấu trúc, và một mô hình nhẹ có khả năng phân loại gắn nhãn phản hồi. Kịch bản pipeline minh họa liên kết + tinh chỉnh; kịch bản router cô lập định tuyến gợi ý đơn thích ứng.

### Ảnh chụp danh mục
```python
CATALOG = {
    "phi-4-mini": {"capabilities": ["general", "summarize"], "priority": 2},
    "deepseek-coder-1.3b": {"capabilities": ["code", "refactor"], "priority": 1},
    "qwen2.5-0.5b": {"capabilities": ["classification", "fast"], "priority": 3}
}
```


### Gợi ý kiểm tra ví dụ
```json
[
    "Refactor this Python function for readability",
    "Summarize the importance of small language models",
    "Classify this feedback: The UI is slow but pretty",
    "Generate a refactored version of a slow Python loop and summarize performance gains."
]
```


### Mở rộng trace (Tùy chọn)
Thêm các dòng JSON trace từng bước cho `models_pipeline.py`:
```python
trace.append({
    "step": step_idx,
    "intent": intent,
    "alias": alias,
    "latency_ms": round((end-start)*1000,2),
    "tokens": getattr(usage,'total_tokens',None)
})
```


### Phương pháp heuristic leo thang (Ý tưởng)
Nếu kế hoạch chứa các từ khóa như "tối ưu hóa", "bảo mật", hoặc độ dài bước > 280 ký tự → leo thang lên mô hình lớn hơn (ví dụ: `gpt-oss-20b`) chỉ cho bước đó.

### Cải tiến tùy chọn

| Khu vực | Cải tiến | Giá trị | Gợi ý |
|---------|----------|---------|-------|
| Bộ nhớ cache | Tái sử dụng đối tượng quản lý + khách hàng | Giảm độ trễ, ít chi phí hơn | Sử dụng `workshop_utils.get_client` |
| Số liệu sử dụng | Thu thập token & độ trễ từng bước | Lập hồ sơ & tối ưu hóa | Đo thời gian mỗi cuộc gọi định tuyến; lưu trong danh sách trace |
| Định tuyến thích ứng | Nhận thức độ tin cậy / chi phí | Cân bằng chất lượng-chi phí tốt hơn | Thêm điểm số: nếu gợi ý > N ký tự hoặc regex khớp với miền → leo thang lên mô hình lớn hơn |
| Đăng ký khả năng động | Tải lại danh mục nóng | Không cần khởi động lại triển khai | Tải `catalog.json` khi runtime; theo dõi dấu thời gian tệp |
| Chiến lược dự phòng | Độ tin cậy khi gặp lỗi | Tăng tính khả dụng | Thử chính → khi gặp ngoại lệ fallback alias |
| Pipeline streaming | Phản hồi sớm | Cải thiện trải nghiệm người dùng | Stream từng bước và đệm đầu vào tinh chỉnh cuối cùng |
| Vector Intent Embeddings | Định tuyến tinh tế hơn | Độ chính xác ý định cao hơn | Nhúng gợi ý, phân cụm & ánh xạ centroid → khả năng |
| Xuất trace | Chuỗi có thể kiểm toán | Tuân thủ/báo cáo | Xuất các dòng JSON: bước, ý định, mô hình, độ trễ_ms, token |
| Mô phỏng chi phí | Ước tính trước đám mây | Lập kế hoạch ngân sách | Gán chi phí giả định/token cho mỗi mô hình & tổng hợp theo nhiệm vụ |
| Chế độ xác định | Tái tạo kết quả | Đánh giá chuẩn ổn định | Env: `temperature=0`, số bước cố định |

#### Ví dụ cấu trúc trace

```python
trace.append({
  "step": idx,
  "intent": intent,
  "alias": alias,
  "latency_ms": round((end-start)*1000,2),
  "tokens": getattr(usage,'total_tokens',None)
})
```


#### Phác thảo leo thang thích ứng

```python
if len(prompt) > 280 or 'compliance' in prompt.lower():
    # escalate to larger reasoning model if available
    alias = 'gpt-oss-20b'
```


#### Tải lại danh mục mô hình nóng

```python
import json, time, os
CATALOG_PATH = 'catalog.json'
last_mtime = 0
def get_catalog():
    global last_mtime, CATALOG
    m = os.path.getmtime(CATALOG_PATH)
    if m != last_mtime:
        CATALOG = json.load(open(CATALOG_PATH))
        last_mtime = m
    return CATALOG
```


Hãy lặp lại dần dần—tránh việc thiết kế quá mức cho các nguyên mẫu ban đầu.

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với các thông tin quan trọng, khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.