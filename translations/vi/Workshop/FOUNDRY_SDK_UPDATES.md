<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "fe36fce800723cb67570f9fc16497d86",
  "translation_date": "2025-10-09T16:38:49+00:00",
  "source_file": "Workshop/FOUNDRY_SDK_UPDATES.md",
  "language_code": "vi"
}
-->
# Cập nhật SDK Foundry Local

## Tổng quan

Đã cập nhật các notebook Workshop và tiện ích để sử dụng đúng **SDK Python Foundry Local chính thức**, theo các mẫu từ:
- https://github.com/microsoft/Foundry-Local
- https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local

## Các tệp đã chỉnh sửa

### 1. `Workshop/samples/workshop_utils.py`

**Thay đổi:**
- ✅ Thêm xử lý lỗi nhập cho gói `foundry-local-sdk`
- ✅ Nâng cao tài liệu với các mẫu SDK chính thức
- ✅ Cải thiện ghi nhật ký với các biểu tượng Unicode (✓, ✗, ⚠)
- ✅ Thêm docstring chi tiết với ví dụ
- ✅ Thông báo lỗi tốt hơn, tham chiếu các lệnh CLI
- ✅ Cập nhật các bình luận để phù hợp với tài liệu SDK chính thức

**Cải tiến chính:**

#### Xử lý lỗi nhập
```python
try:
    from foundry_local import FoundryLocalManager
except ImportError:
    raise ImportError(
        "foundry-local-sdk is required. Install with: pip install foundry-local-sdk"
    )
```

#### Nâng cao hàm `get_client()`
- Thêm tài liệu chi tiết về mẫu khởi tạo SDK
- Làm rõ rằng `FoundryLocalManager` tự động khởi động dịch vụ
- Giải thích cách giải quyết alias mô hình thành các biến thể tối ưu hóa phần cứng
- Cải thiện ghi nhật ký với thông tin endpoint
- Thông báo lỗi tốt hơn, gợi ý các bước khắc phục sự cố

#### Nâng cao hàm `chat_once()`
- Thêm docstring chi tiết với ví dụ sử dụng
- Làm rõ khả năng tương thích với SDK OpenAI
- Tài liệu hỗ trợ streaming (thông qua kwargs)
- Thông báo lỗi tốt hơn với gợi ý lệnh CLI
- Thêm ghi chú về kiểm tra tính khả dụng của mô hình

### 2. `Workshop/notebooks/session06_models_router.ipynb`

**Thay đổi:**
- ✅ Cập nhật tất cả các ô markdown với tham chiếu SDK
- ✅ Nâng cao bình luận mã với giải thích mẫu SDK
- ✅ Cải thiện tài liệu và giải thích trong ô
- ✅ Thêm hướng dẫn khắc phục sự cố
- ✅ Cập nhật danh mục mô hình (thay thế 'gpt-oss-20b' bằng 'phi-3.5-mini')
- ✅ Định dạng đầu ra tốt hơn với các chỉ báo trực quan
- ✅ Thêm liên kết và tham chiếu SDK xuyên suốt

**Cập nhật từng ô:**

#### Ô 1 (Tiêu đề)
- Thêm liên kết tài liệu SDK
- Tham chiếu các kho GitHub chính thức

#### Ô 2 (Kịch bản)
- Định dạng lại với các bước đánh số
- Làm rõ mẫu định tuyến dựa trên ý định
- Nhấn mạnh lợi ích của thực thi cục bộ

#### Ô 3 (Cài đặt phụ thuộc)
- Thêm giải thích về những gì mỗi gói cung cấp
- Tài liệu khả năng của SDK (giải quyết alias, tối ưu hóa phần cứng)

#### Ô 4 (Thiết lập môi trường)
- Nâng cao docstring hàm
- Thêm bình luận nội tuyến giải thích mẫu SDK
- Tài liệu cấu trúc danh mục mô hình
- Làm rõ việc khớp ưu tiên/khả năng

#### Ô 5 (Kiểm tra danh mục)
- Thêm dấu kiểm trực quan (✓)
- Định dạng đầu ra tốt hơn

#### Ô 6 (Kiểm tra phát hiện ý định)
- Định dạng lại đầu ra theo kiểu bảng
- Hiển thị cả ý định và mô hình được chọn

#### Ô 7 (Hàm định tuyến)
- Giải thích mẫu SDK toàn diện
- Tài liệu luồng khởi tạo
- Liệt kê tất cả các tính năng (retry, tracking, lỗi)
- Thêm liên kết tham chiếu SDK

#### Ô 8 (Demo theo lô)
- Giải thích nâng cao về những gì mong đợi
- Thêm phần khắc phục sự cố
- Bao gồm các lệnh CLI để gỡ lỗi
- Định dạng hiển thị đầu ra tốt hơn

### 3. `Workshop/notebooks/session06_README.md` (Tệp mới)

**Tạo tài liệu toàn diện bao gồm:**

1. **Tổng quan**: Sơ đồ kiến trúc và giải thích thành phần
2. **Tích hợp SDK**: Ví dụ mã theo các mẫu chính thức
3. **Yêu cầu trước**: Hướng dẫn thiết lập từng bước
4. **Cách sử dụng**: Cách chạy và tùy chỉnh notebook
5. **Alias mô hình**: Giải thích các biến thể tối ưu hóa phần cứng
6. **Khắc phục sự cố**: Các vấn đề thường gặp và giải pháp
7. **Mở rộng**: Cách thêm ý định, mô hình và logic tùy chỉnh
8. **Mẹo hiệu suất**: Thực tiễn tốt nhất cho sử dụng sản xuất
9. **Tài nguyên**: Liên kết đến tài liệu chính thức và cộng đồng

## Triển khai mẫu SDK

### Mẫu chính thức (từ tài liệu Foundry Local)

```python
from foundry_local import FoundryLocalManager
from openai import OpenAI

# By using an alias, the most suitable model will be downloaded
alias = "phi-3.5-mini"

# Create a FoundryLocalManager instance
manager = FoundryLocalManager(alias)

# Configure the client to use the local Foundry service
client = OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key
)

# Generate completion
stream = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[{"role": "user", "content": "What is AI?"}],
    stream=True
)
```

### Triển khai của chúng tôi (trong workshop_utils)

```python
def get_client(alias: str, endpoint: Optional[str] = None):
    """Initialize FoundryLocalManager and OpenAI client (with caching)"""
    # Initialize manager (starts service if needed)
    manager = FoundryLocalManager(alias, endpoint=endpoint) if endpoint else FoundryLocalManager(alias)
    
    # Create OpenAI-compatible client
    client = OpenAI(
        base_url=manager.endpoint,
        api_key=manager.api_key
    )
    
    # Resolve model ID
    model_id = manager.get_model_info(alias).id
    
    return manager, client, model_id

def chat_once(alias: str, messages: List[dict], **kwargs):
    """Execute chat completion with retry logic"""
    _, client, model_id = get_client(alias)
    resp = client.chat.completions.create(model=model_id, messages=messages, **kwargs)
    return resp.choices[0].message.content, resp.usage
```

**Lợi ích của cách tiếp cận của chúng tôi:**
- ✅ Tuân theo mẫu SDK chính thức một cách chính xác
- ✅ Thêm caching để tránh khởi tạo lặp lại
- ✅ Bao gồm logic retry để tăng độ bền sản xuất
- ✅ Hỗ trợ theo dõi sử dụng token
- ✅ Cung cấp thông báo lỗi tốt hơn
- ✅ Tương thích với các ví dụ chính thức

## Thay đổi danh mục mô hình

### Trước
```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'gpt-oss-20b': {'capabilities':['code','refactor'],'priority':1},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':3},
}
```

### Sau
```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini': {'capabilities':['code','refactor'],'priority':3},
}
```

**Lý do:** Thay thế 'gpt-oss-20b' (alias không chuẩn) bằng 'phi-3.5-mini' (alias chính thức của Foundry Local).

## Phụ thuộc

### Cập nhật requirements.txt

Tệp requirements.txt của Workshop đã bao gồm:
```
foundry-local-sdk
openai>=1.30.0
```

Đây là các gói duy nhất cần thiết cho tích hợp Foundry Local.

## Kiểm tra các cập nhật

### 1. Xác minh Foundry Local đang chạy

```bash
# Windows
foundry service status

# If not running
foundry service start
```

### 2. Kiểm tra các mô hình khả dụng

```bash
foundry model ls
```

Đảm bảo các mô hình này khả dụng hoặc sẽ tự động tải xuống:
- phi-4-mini
- phi-3.5-mini
- qwen2.5-0.5b

### 3. Chạy Notebook

```bash
cd Workshop
jupyter notebook notebooks/session06_models_router.ipynb
```

Hoặc mở trong VS Code và chạy tất cả các ô.

### 4. Hành vi mong đợi

**Ô 1 (Cài đặt):** Cài đặt gói thành công  
**Ô 2 (Thiết lập):** Không có lỗi, nhập hoạt động  
**Ô 3 (Xác minh):** Hiển thị ✓ với danh sách mô hình  
**Ô 4 (Kiểm tra ý định):** Hiển thị kết quả phát hiện ý định  
**Ô 5 (Định tuyến):** Hiển thị ✓ Hàm định tuyến sẵn sàng  
**Ô 6 (Thực thi):** Định tuyến prompt đến mô hình, hiển thị kết quả  

### 5. Khắc phục lỗi kết nối

Nếu bạn thấy `APIConnectionError: Connection error`:

```bash
# Check service
foundry service status

# Check endpoint
curl http://localhost:55769/health

# Restart if needed
foundry service stop
foundry service start
```

## Biến môi trường

Các biến môi trường sau được hỗ trợ:

| Biến | Mặc định | Mô tả |
|------|----------|-------|
| `SHOW_USAGE` | `0` | Đặt thành `1` để in sử dụng token |
| `RETRY_ON_FAIL` | `1` | Bật logic retry |
| `RETRY_BACKOFF` | `1.0` | Độ trễ retry ban đầu (giây) |
| `FOUNDRY_LOCAL_ENDPOINT` | Auto | Ghi đè endpoint dịch vụ |

### Ví dụ sử dụng

```python
import os

# Enable token tracking
os.environ['SHOW_USAGE'] = '1'

# Adjust retry timing
os.environ['RETRY_BACKOFF'] = '2.0'

# Use custom endpoint
os.environ['FOUNDRY_LOCAL_ENDPOINT'] = 'http://localhost:8000'
```

## Di chuyển từ mẫu cũ

Nếu bạn có mã hiện tại sử dụng các cuộc gọi API trực tiếp, đây là cách di chuyển:

### Trước (API trực tiếp)
```python
import requests

response = requests.post(
    'http://localhost:8000/v1/chat/completions',
    json={
        'model': 'phi-4-mini',
        'messages': [{'role': 'user', 'content': 'Hello'}]
    }
)
```

### Sau (SDK)
```python
from foundry_local import FoundryLocalManager
from openai import OpenAI

manager = FoundryLocalManager('phi-4-mini')
client = OpenAI(base_url=manager.endpoint, api_key=manager.api_key)

response = client.chat.completions.create(
    model=manager.get_model_info('phi-4-mini').id,
    messages=[{'role': 'user', 'content': 'Hello'}]
)
```

### Lợi ích của việc di chuyển
- ✅ Quản lý dịch vụ tự động
- ✅ Giải quyết alias mô hình
- ✅ Lựa chọn tối ưu hóa phần cứng
- ✅ Xử lý lỗi tốt hơn
- ✅ Tương thích với SDK OpenAI
- ✅ Hỗ trợ streaming

## Tham khảo

### Tài liệu chính thức
- **GitHub Foundry Local**: https://github.com/microsoft/Foundry-Local
- **Nguồn SDK Python**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **Tham chiếu CLI**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md
- **REST API**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-rest.md
- **Khắc phục sự cố**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-troubleshooting.md

### Tài nguyên Workshop
- **README Phiên 06**: `Workshop/notebooks/session06_README.md`
- **Tiện ích Workshop**: `Workshop/samples/workshop_utils.py`
- **Notebook mẫu**: `Workshop/notebooks/session06_models_router.ipynb`

### Cộng đồng
- **Discord**: https://aka.ms/foundry-local-discord
- **GitHub Issues**: https://github.com/microsoft/Foundry-Local/issues

## Các bước tiếp theo

1. **Xem lại thay đổi**: Đọc qua các tệp đã cập nhật  
2. **Kiểm tra Notebook**: Chạy session06_models_router.ipynb  
3. **Xác minh SDK**: Đảm bảo foundry-local-sdk đã được cài đặt  
4. **Kiểm tra dịch vụ**: Xác nhận Foundry Local đang chạy  
5. **Khám phá tài liệu**: Đọc session06_README.md mới  

## Tóm tắt

Những cập nhật này đảm bảo tài liệu Workshop tuân theo **mẫu SDK Foundry Local chính thức** đúng như đã được ghi trong kho GitHub. Tất cả các ví dụ mã, tài liệu và tiện ích giờ đây phù hợp với các thực tiễn tốt nhất được Microsoft khuyến nghị cho triển khai mô hình AI cục bộ.

Các thay đổi cải thiện:
- ✅ **Độ chính xác**: Sử dụng mẫu SDK chính thức  
- ✅ **Tài liệu**: Giải thích và ví dụ toàn diện  
- ✅ **Xử lý lỗi**: Thông báo và hướng dẫn khắc phục sự cố tốt hơn  
- ✅ **Khả năng duy trì**: Tuân theo quy ước chính thức  
- ✅ **Trải nghiệm người dùng**: Hướng dẫn rõ ràng và hỗ trợ gỡ lỗi  

---

**Cập nhật:** Ngày 8 tháng 10 năm 2025  
**Phiên bản SDK:** foundry-local-sdk (mới nhất)  
**Nhánh Workshop:** Reactor  

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp của con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.