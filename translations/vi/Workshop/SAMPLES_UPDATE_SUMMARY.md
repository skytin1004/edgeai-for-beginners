<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5506309052b4f332914e36b518f11b14",
  "translation_date": "2025-10-09T16:58:51+00:00",
  "source_file": "Workshop/SAMPLES_UPDATE_SUMMARY.md",
  "language_code": "vi"
}
-->
# Mẫu Workshop - Tóm tắt cập nhật SDK Foundry Local

## Tổng quan

Tất cả các mẫu Python trong thư mục `Workshop/samples` đã được cập nhật để tuân theo các thực hành tốt nhất của SDK Foundry Local và đảm bảo tính nhất quán trong toàn bộ workshop.

**Ngày**: 8 tháng 10, 2025  
**Phạm vi**: 9 tệp Python trong 6 buổi workshop  
**Trọng tâm chính**: Xử lý lỗi, tài liệu, mẫu SDK, trải nghiệm người dùng

---

## Các tệp đã cập nhật

### Buổi 01: Bắt đầu
- ✅ `chat_bootstrap.py` - Ví dụ cơ bản về chat và streaming

### Buổi 02: Giải pháp RAG
- ✅ `rag_pipeline.py` - Triển khai RAG với embeddings
- ✅ `rag_eval_ragas.py` - Đánh giá RAG với các chỉ số RAGAS

### Buổi 03: Mô hình mã nguồn mở
- ✅ `benchmark_oss_models.py` - Đánh giá nhiều mô hình

### Buổi 04: Mô hình tiên tiến
- ✅ `model_compare.py` - So sánh SLM và LLM

### Buổi 05: Tác nhân AI
- ✅ `agents_orchestrator.py` - Điều phối nhiều tác nhân

### Buổi 06: Mô hình như công cụ
- ✅ `models_router.py` - Định tuyến mô hình dựa trên ý định
- ✅ `models_pipeline.py` - Pipeline định tuyến nhiều bước

### Hạ tầng hỗ trợ
- ✅ `workshop_utils.py` - Đã tuân theo các thực hành tốt nhất (không cần thay đổi)

---

## Cải tiến chính

### 1. Nâng cao xử lý lỗi

**Trước:**
```python
manager, client, model_id = get_client(alias)
```

**Sau:**
```python
try:
    manager, client, model_id = get_client(alias, endpoint=endpoint)
except Exception as e:
    print(f"[ERROR] Failed to initialize Foundry Local client: {e}")
    print("[INFO] Ensure Foundry Local is running: foundry service status")
    sys.exit(1)
```

**Lợi ích:**
- Xử lý lỗi mượt mà với thông báo lỗi rõ ràng
- Gợi ý khắc phục lỗi có thể hành động
- Mã thoát phù hợp cho scripting

### 2. Quản lý import tốt hơn

**Trước:**
```python
from sentence_transformers import SentenceTransformer
```

**Sau:**
```python
try:
    from sentence_transformers import SentenceTransformer
except ImportError:
    print("[ERROR] sentence-transformers is required. Install with: pip install sentence-transformers")
    sys.exit(1)
```

**Lợi ích:**
- Hướng dẫn rõ ràng khi thiếu dependencies
- Ngăn chặn lỗi import khó hiểu
- Hướng dẫn cài đặt thân thiện với người dùng

### 3. Tài liệu toàn diện

**Đã thêm vào tất cả các mẫu:**
- Tài liệu về biến môi trường trong docstrings
- Liên kết tham khảo SDK
- Ví dụ sử dụng
- Tài liệu chi tiết về hàm/tham số
- Gợi ý kiểu dữ liệu để hỗ trợ IDE tốt hơn

**Ví dụ:**
```python
def pipeline(task: str) -> Dict[str, Any]:
    """Execute multi-step routed pipeline for complex task.
    
    Args:
        task: User task description
    
    Returns:
        Dictionary with plan, step outputs, and final summary
    
    Raises:
        Exception: If any pipeline stage fails
    """
```

### 4. Phản hồi người dùng được cải thiện

**Đã thêm logging thông tin:**
```python
print(f"[INFO] Using model alias: {alias} -> id: {model_id}")
print(f"[INFO] Endpoint: {manager.endpoint}")
print(f"[INFO] Loaded model: {alias} -> {model_id}")
```

**Chỉ báo tiến độ:**
```python
print(f"[INFO] Benchmarking {alias}...")
print(f"  Round {round_num + 1}/{ROUNDS}: {latency:.3f}s")
print(f"[INFO] Completed {alias}\n")
```

**Đầu ra có cấu trúc:**
```python
print("\n[BENCHMARK RESULTS]")
print(json.dumps(summary, indent=2))
```

### 5. Đánh giá mạnh mẽ

**Cải tiến buổi 03:**
- Xử lý lỗi theo từng mô hình (tiếp tục khi gặp lỗi)
- Báo cáo tiến độ chi tiết
- Thực hiện đúng các vòng khởi động
- Hỗ trợ đo lường độ trễ token đầu tiên
- Phân tách rõ ràng các giai đoạn

### 6. Gợi ý kiểu dữ liệu nhất quán

**Đã thêm vào toàn bộ:**
```python
from typing import Dict, List, Tuple, Any, Optional

def run(alias: str) -> Tuple[float, str, Optional[int]]:
    """Run comparison for given model alias."""
```

**Lợi ích:**
- Tự động hoàn thành tốt hơn trong IDE
- Phát hiện lỗi sớm
- Mã tự tài liệu hóa

### 7. Bộ định tuyến mô hình nâng cao

**Cải tiến buổi 06:**
- Tài liệu chi tiết về phát hiện ý định
- Giải thích thuật toán chọn mô hình
- Logging định tuyến chi tiết
- Định dạng đầu ra kiểm tra
- Khôi phục lỗi trong kiểm tra theo lô

### 8. Điều phối nhiều tác nhân

**Cải tiến buổi 05:**
- Báo cáo tiến độ theo từng giai đoạn
- Xử lý lỗi theo từng tác nhân
- Cấu trúc pipeline rõ ràng
- Tài liệu quản lý bộ nhớ tốt hơn

---

## Danh sách kiểm tra kiểm thử

### Điều kiện tiên quyết
```bash
# Ensure Foundry Local is running
foundry service status

# Load required models
foundry model run phi-4-mini
foundry model run qwen2.5-0.5b

# Install dependencies
pip install -r Workshop/requirements.txt
```

### Kiểm tra từng mẫu

#### Buổi 01
```bash
cd Workshop/samples/session01
python chat_bootstrap.py "What is edge AI?"
```

#### Buổi 02
```bash
cd Workshop/samples/session02

# RAG pipeline
python rag_pipeline.py

# RAG evaluation (requires ragas)
set RAG_QUESTION="What is local inference?"
python rag_eval_ragas.py
```

#### Buổi 03
```bash
cd Workshop/samples/session03

# Quick benchmark (2 rounds)
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=2
python benchmark_oss_models.py
```

#### Buổi 04
```bash
cd Workshop/samples/session04

# SLM vs LLM comparison
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b
python model_compare.py
```

#### Buổi 05
```bash
cd Workshop/samples/session05

# Multi-agent orchestration
set AGENT_QUESTION="Why use local AI for healthcare?"
python agents_orchestrator.py
```

#### Buổi 06
```bash
cd Workshop/samples/session06

# Intent-based routing
python models_router.py

# Multi-step pipeline
set PIPELINE_TASK="Create a Python function and explain its performance"
python models_pipeline.py
```

---

## Tham chiếu biến môi trường

### Toàn cục (Tất cả các mẫu)
| Biến | Mô tả | Mặc định |
|------|-------|----------|
| `FOUNDRY_LOCAL_ALIAS` | Bí danh mô hình sử dụng | Thay đổi theo mẫu |
| `FOUNDRY_LOCAL_ENDPOINT` | Ghi đè endpoint dịch vụ | Tự động phát hiện |
| `SHOW_USAGE` | Hiển thị sử dụng token | `0` |
| `RETRY_ON_FAIL` | Bật logic thử lại | `1` |
| `RETRY_BACKOFF` | Độ trễ thử lại ban đầu | `1.0` |

### Cụ thể theo mẫu
| Biến | Sử dụng bởi | Mô tả |
|------|-------------|-------|
| `EMBED_MODEL` | Buổi 02 | Tên mô hình embedding |
| `RAG_QUESTION` | Buổi 02 | Câu hỏi kiểm tra cho RAG |
| `BENCH_MODELS` | Buổi 03 | Các mô hình đánh giá, phân tách bằng dấu phẩy |
| `BENCH_ROUNDS` | Buổi 03 | Số vòng đánh giá |
| `BENCH_PROMPT` | Buổi 03 | Prompt kiểm tra cho đánh giá |
| `BENCH_STREAM` | Buổi 03 | Đo độ trễ token đầu tiên |
| `SLM_ALIAS` | Buổi 04 | Mô hình ngôn ngữ nhỏ |
| `LLM_ALIAS` | Buổi 04 | Mô hình ngôn ngữ lớn |
| `COMPARE_PROMPT` | Buổi 04 | Prompt kiểm tra so sánh |
| `AGENT_MODEL_PRIMARY` | Buổi 05 | Mô hình tác nhân chính |
| `AGENT_MODEL_EDITOR` | Buổi 05 | Mô hình tác nhân chỉnh sửa |
| `AGENT_QUESTION` | Buổi 05 | Câu hỏi kiểm tra cho tác nhân |
| `PIPELINE_TASK` | Buổi 06 | Nhiệm vụ cho pipeline |

---

## Thay đổi phá vỡ

**Không có** - Tất cả các thay đổi đều tương thích ngược.

Các script hiện tại sẽ tiếp tục hoạt động. Các tính năng mới bao gồm:
- Biến môi trường tùy chọn
- Thông báo lỗi nâng cao (không làm hỏng chức năng)
- Logging bổ sung (có thể tắt)
- Gợi ý kiểu dữ liệu tốt hơn (không ảnh hưởng đến runtime)

---

## Các thực hành tốt nhất đã triển khai

### 1. Luôn sử dụng Workshop Utils
```python
from workshop_utils import get_client, chat_once

# Provides caching, retry, and endpoint management
manager, client, model_id = get_client(alias, endpoint=endpoint)
```

### 2. Mẫu xử lý lỗi phù hợp
```python
try:
    # Initialize client
    manager, client, model_id = get_client(alias)
except Exception as e:
    print(f"[ERROR] Initialization failed: {e}")
    print("[INFO] Check: foundry service status")
    sys.exit(1)
```

### 3. Logging thông tin
```python
print(f"[INFO] Starting process...")  # Info
print(f"[ERROR] Operation failed: {e}")  # Errors
print(f"[RESULT] Final output")  # Results
```

### 4. Gợi ý kiểu dữ liệu
```python
from typing import Dict, List, Optional

def process(data: List[str]) -> Dict[str, Any]:
    """Process data with type safety."""
```

### 5. Docstrings toàn diện
```python
def function(arg: str) -> str:
    """Short description.
    
    Args:
        arg: Argument description
    
    Returns:
        Return value description
    
    Raises:
        Exception: When it fails
    """
```

### 6. Hỗ trợ biến môi trường
```python
import os

alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-4-mini")
endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")  # None if not set
```

### 7. Suy giảm mượt mà
```python
# In benchmarks - continue on individual failures
for model in models:
    try:
        result = benchmark(model)
        results.append(result)
    except Exception as e:
        print(f"[ERROR] {model} failed: {e}")
        print(f"[INFO] Skipping {model}...")
```

---

## Các vấn đề thường gặp & giải pháp

### Vấn đề: Lỗi import
**Giải pháp:** Cài đặt các dependencies bị thiếu
```bash
pip install sentence-transformers ragas datasets numpy
```

### Vấn đề: Lỗi kết nối
**Giải pháp:** Đảm bảo Foundry Local đang chạy
```bash
foundry service status
foundry model run phi-4-mini
```

### Vấn đề: Không tìm thấy mô hình
**Giải pháp:** Kiểm tra các mô hình có sẵn
```bash
foundry model ls
foundry model download <alias>
```

### Vấn đề: Hiệu suất chậm
**Giải pháp:** Sử dụng mô hình nhỏ hơn hoặc điều chỉnh tham số
```bash
set FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b
set BENCH_ROUNDS=2
```

---

## Các bước tiếp theo

### 1. Kiểm tra tất cả các mẫu
Thực hiện danh sách kiểm tra kiểm thử ở trên để xác minh tất cả các mẫu hoạt động chính xác.

### 2. Cập nhật tài liệu
- Cập nhật các tệp markdown của buổi với các ví dụ mới
- Thêm phần khắc phục sự cố vào README chính
- Tạo hướng dẫn tham khảo nhanh

### 3. Tạo kiểm thử tích hợp
```python
# Workshop/tests/test_samples.py
def test_all_samples():
    """Run smoke tests on all samples."""
```

### 4. Thêm đánh giá hiệu suất
Theo dõi các cải tiến hiệu suất từ việc nâng cao xử lý lỗi.

### 5. Phản hồi người dùng
Thu thập phản hồi từ người tham gia workshop về:
- Độ rõ ràng của thông báo lỗi
- Độ đầy đủ của tài liệu
- Dễ sử dụng

---

## Tài nguyên

- **Foundry Local SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **Tham khảo nhanh**: `Workshop/FOUNDRY_SDK_QUICKREF.md`
- **Ghi chú di chuyển**: `Workshop/SDK_MIGRATION_NOTES.md`
- **Kho chính**: https://github.com/microsoft/Foundry-Local

---

## Bảo trì

### Thêm mẫu mới
Tuân theo các mẫu này khi tạo mẫu mới:

1. Sử dụng `workshop_utils` để quản lý client
2. Thêm xử lý lỗi toàn diện
3. Bao gồm hỗ trợ biến môi trường
4. Thêm gợi ý kiểu dữ liệu và docstrings
5. Cung cấp logging thông tin
6. Bao gồm ví dụ sử dụng trong docstring
7. Liên kết đến tài liệu SDK

### Xem xét cập nhật
Khi xem xét các cập nhật mẫu, kiểm tra:
- [ ] Xử lý lỗi trên tất cả các thao tác I/O
- [ ] Gợi ý kiểu dữ liệu trên các hàm công khai
- [ ] Docstrings toàn diện
- [ ] Tài liệu biến môi trường
- [ ] Phản hồi thông tin cho người dùng
- [ ] Liên kết tham khảo SDK
- [ ] Phong cách mã nhất quán

---

**Tóm tắt**: Tất cả các mẫu Python trong Workshop hiện tuân theo các thực hành tốt nhất của SDK Foundry Local với xử lý lỗi nâng cao, tài liệu toàn diện và trải nghiệm người dùng được cải thiện. Không có thay đổi phá vỡ - tất cả chức năng hiện tại được bảo toàn và nâng cao.

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với các thông tin quan trọng, khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.