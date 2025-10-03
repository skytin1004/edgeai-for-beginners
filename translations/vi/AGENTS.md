<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec4ff1735cf3d48aed41d924c0a0ff29",
  "translation_date": "2025-10-03T08:39:28+00:00",
  "source_file": "AGENTS.md",
  "language_code": "vi"
}
-->
# AGENTS.md

## Tổng quan dự án

EdgeAI for Beginners là một kho tài liệu giáo dục toàn diện, hướng dẫn phát triển Edge AI với các Mô hình Ngôn ngữ Nhỏ (SLMs). Khóa học bao gồm các kiến thức cơ bản về EdgeAI, triển khai mô hình, kỹ thuật tối ưu hóa và các ứng dụng sẵn sàng cho sản xuất sử dụng Microsoft Foundry Local và các framework AI khác nhau.

**Công nghệ chính:**
- Python 3.8+ (ngôn ngữ chính cho các mẫu AI/ML)
- .NET C# (mẫu AI/ML)
- JavaScript/Node.js với Electron (cho ứng dụng máy tính để bàn)
- Microsoft Foundry Local SDK
- Microsoft Windows ML 
- VSCode AI Toolkit
- OpenAI SDK
- Framework AI: LangChain, Semantic Kernel, Chainlit
- Tối ưu hóa mô hình: Llama.cpp, Microsoft Olive, OpenVINO, Apple MLX

**Loại kho:** Kho tài liệu giáo dục với 8 module và 10 ứng dụng mẫu toàn diện

**Kiến trúc:** Lộ trình học đa module với các mẫu thực hành minh họa các mô hình triển khai Edge AI

## Cấu trúc kho

```
edgeai-for-beginners/
├── introduction.md          # Course introduction and overview
├── Module01-07/            # Core educational modules (Markdown)
├── Module08/               # Foundry Local toolkit with 10 samples
│   ├── samples/01-06/     # Foundation samples (Python)
│   ├── samples/07/        # API client (Python)
│   ├── samples/08/        # Windows 11 chat app (Electron)
│   └── samples/09-10/     # Advanced multi-agent systems (Python)
├── translations/          # Multi-language translations (50+ languages)
├── translated_images/     # Localized images
└── imgs/                  # Course images and assets
```

## Lệnh thiết lập

### Thiết lập kho

```bash
# Clone the repository
git clone https://github.com/microsoft/edgeai-for-beginners.git
cd edgeai-for-beginners

# No build step required - this is primarily an educational content repository
```

### Thiết lập mẫu Python (Module08 và các mẫu Python)

```bash
# Create and activate virtual environment
python -m venv .venv
# On Windows
.venv\Scripts\activate
# On macOS/Linux
source .venv/bin/activate

# Install dependencies for Module08 samples
cd Module08
pip install -r requirements.txt
```

### Thiết lập mẫu Node.js (Mẫu 08 - Ứng dụng Chat trên Windows)

```bash
cd Module08/samples/08
npm install

# Start in development mode
npm run dev

# Build for production
npm run build

# Create installer
npm run dist
```

### Thiết lập Foundry Local

Foundry Local cần thiết để chạy các mẫu trong Module08:

```bash
# Start Foundry Local service with a model
foundry model run phi-4-mini

# Verify service is running
curl http://localhost:8000/health
```

## Quy trình phát triển

### Phát triển nội dung

Kho này chủ yếu chứa **nội dung giáo dục bằng Markdown**. Khi thực hiện thay đổi:

1. Chỉnh sửa các tệp `.md` trong thư mục module tương ứng
2. Tuân theo các mẫu định dạng hiện có
3. Đảm bảo các ví dụ mã chính xác và đã được kiểm tra
4. Cập nhật nội dung dịch tương ứng nếu cần (hoặc để tự động hóa xử lý)

### Phát triển ứng dụng mẫu

Đối với các mẫu Python (mẫu 01-07, 09-10):
```bash
cd Module08
python samples/01/chat_quickstart.py "Test message"
```

Đối với mẫu Electron (mẫu 08):
```bash
cd Module08/samples/08
npm run dev  # Development with hot reload
```

### Kiểm tra ứng dụng mẫu

Các mẫu Python không có kiểm tra tự động nhưng có thể được xác thực bằng cách chạy chúng:
```bash
# Test basic chat functionality
python samples/01/chat_quickstart.py "Hello"

# Test with specific model
set MODEL=phi-4-mini
python samples/02/openai_sdk_client.py
```

Mẫu Electron có cơ sở hạ tầng kiểm tra:
```bash
cd Module08/samples/08
npm test           # Run unit tests
npm run test:e2e   # Run end-to-end tests
npm run lint       # Check code style
```

## Hướng dẫn kiểm tra

### Xác thực nội dung

Kho sử dụng quy trình dịch tự động. Không cần kiểm tra thủ công cho các bản dịch.

**Xác thực thủ công cho thay đổi nội dung:**
1. Xem trước hiển thị Markdown bằng cách xem trước các tệp `.md`
2. Xác minh tất cả các liên kết dẫn đến mục tiêu hợp lệ
3. Kiểm tra các đoạn mã trong tài liệu
4. Đảm bảo hình ảnh tải đúng cách

### Kiểm tra ứng dụng mẫu

**Module08/samples/08 (ứng dụng Electron) có kiểm tra toàn diện:**
```bash
cd Module08/samples/08

# Run all tests
npm test

# Run unit tests only
npm test -- --testPathPattern=unit

# Run integration tests
npm run test:integration

# Run E2E tests
npm run test:e2e

# Check test coverage
npm test -- --coverage
```

**Các mẫu Python cần được kiểm tra thủ công:**
```bash
# Each sample can be run directly
python samples/01/chat_quickstart.py "Test prompt"
python samples/04/chainlit_rag.py
python samples/09/multi_agent_system.py
```

## Hướng dẫn về phong cách mã

### Nội dung Markdown

- Sử dụng cấu trúc tiêu đề nhất quán (# cho tiêu đề, ## cho các phần chính, ### cho các phần phụ)
- Bao gồm các khối mã với định danh ngôn ngữ: ```python, ```bash, ```javascript
- Tuân theo định dạng hiện có cho bảng, danh sách và nhấn mạnh
- Giữ các dòng dễ đọc (khoảng ~80-100 ký tự, nhưng không bắt buộc)
- Sử dụng liên kết tương đối cho các tham chiếu nội bộ

### Phong cách mã Python

- Tuân theo quy ước PEP 8
- Sử dụng gợi ý kiểu dữ liệu khi phù hợp
- Bao gồm docstring cho các hàm và lớp
- Sử dụng tên biến có ý nghĩa
- Giữ các hàm tập trung và ngắn gọn

### Phong cách mã JavaScript/Node.js

```bash
# Electron sample follows ESLint configuration
cd Module08/samples/08
npm run lint        # Check for style issues
npm run lint:fix    # Auto-fix style issues
npm run format      # Format with Prettier
```

**Quy ước chính:**
- Cấu hình ESLint được cung cấp trong mẫu 08
- Prettier để định dạng mã
- Sử dụng cú pháp ES6+ hiện đại
- Tuân theo các mẫu hiện có trong cơ sở mã

## Hướng dẫn Pull Request

### Định dạng tiêu đề
```
[ModuleXX] Brief description of change
```
hoặc
```
[Module08/samples/XX] Description for sample changes
```

### Trước khi gửi

**Đối với thay đổi nội dung:**
- Xem trước tất cả các tệp Markdown đã chỉnh sửa
- Xác minh liên kết và hình ảnh hoạt động
- Kiểm tra lỗi chính tả và ngữ pháp

**Đối với thay đổi mã mẫu (Module08/samples/08):**
```bash
npm run lint
npm test
```

**Đối với thay đổi mẫu Python:**
- Kiểm tra mẫu chạy thành công
- Xác minh xử lý lỗi hoạt động
- Kiểm tra khả năng tương thích với Foundry Local

### Quy trình xem xét

- Thay đổi nội dung giáo dục được xem xét về độ chính xác và rõ ràng
- Các mẫu mã được kiểm tra về chức năng
- Cập nhật dịch thuật được xử lý tự động bởi GitHub Actions

## Hệ thống dịch thuật

**QUAN TRỌNG:** Kho này sử dụng dịch thuật tự động qua GitHub Actions.

- Các bản dịch nằm trong thư mục `/translations/` (50+ ngôn ngữ)
- Tự động hóa qua workflow `co-op-translator.yml`
- **KHÔNG chỉnh sửa thủ công các tệp dịch** - chúng sẽ bị ghi đè
- Chỉ chỉnh sửa các tệp nguồn tiếng Anh trong thư mục gốc và module
- Các bản dịch được tạo tự động khi đẩy lên nhánh `main`

## Tích hợp Foundry Local

Hầu hết các mẫu trong Module08 yêu cầu Microsoft Foundry Local đang chạy:

### Khởi động Foundry Local
```bash
# Start Foundry Local 
foundry service start

#foundry service host and port are displayed after running this command or `foundry service status`

# Run a specific model
foundry model run phi-4-mini

# Or run with different models
foundry model run qwen2.5-coder-0.5b
foundry model run mistral-7b
```

### Xác minh Foundry Local
```bash
# Check service health
curl http://127.0.0.1:55769/

# the Port and PID will be displayed when running `foundry service start`

# List loaded models
curl http://localhost:55769/v1/models
```

### Biến môi trường cho các mẫu

Hầu hết các mẫu sử dụng các biến môi trường sau:
```bash
# Foundry Local configuration (defaults work for most cases)
set BASE_URL=http://localhost:55769
set MODEL=phi-4-mini
set API_KEY=

# For Azure OpenAI fallback (optional)
set AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
set AZURE_OPENAI_API_KEY=your-api-key
set AZURE_OPENAI_API_VERSION=2024-08-01-preview
```

## Xây dựng và triển khai

### Triển khai nội dung

Kho này chủ yếu là tài liệu - không yêu cầu quy trình xây dựng cho nội dung.

### Xây dựng ứng dụng mẫu

**Ứng dụng Electron (Module08/samples/08):**
```bash
cd Module08/samples/08

# Development build
npm run dev

# Production build
npm run build

# Create Windows installer
npm run dist

# Create portable executable
npm run pack
```

**Mẫu Python:**
Không có quy trình xây dựng - các mẫu được chạy trực tiếp bằng trình thông dịch Python.

## Các vấn đề thường gặp và cách khắc phục

### Foundry Local không chạy
**Vấn đề:** Các mẫu gặp lỗi kết nối

**Giải pháp:**
```bash
# Start Foundry Local service
foundry model run phi-4-mini

# Verify it's running
curl http://localhost:55769/health
```

### Vấn đề môi trường ảo Python
**Vấn đề:** Lỗi nhập module

**Giải pháp:**
```bash
# Ensure virtual environment is activated
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

### Vấn đề xây dựng Electron
**Vấn đề:** npm install hoặc lỗi xây dựng

**Giải pháp:**
```bash
cd Module08/samples/08
# Clean install
npm run clean
rm -rf node_modules package-lock.json
npm install
```

### Xung đột quy trình dịch thuật
**Vấn đề:** PR dịch thuật xung đột với thay đổi của bạn

**Giải pháp:**
- Chỉ chỉnh sửa các tệp nguồn tiếng Anh
- Để quy trình dịch thuật tự động xử lý các bản dịch
- Nếu xảy ra xung đột, hợp nhất `main` vào nhánh của bạn sau khi các bản dịch được hợp nhất

## Tài nguyên bổ sung

### Lộ trình học tập
- **Lộ trình cơ bản:** Module 01-02 (7-9 giờ)
- **Lộ trình trung cấp:** Module 03-04 (9-11 giờ)
- **Lộ trình nâng cao:** Module 05-07 (12-15 giờ)
- **Lộ trình chuyên gia:** Module 08 (8-10 giờ)

### Nội dung chính của module
- **Module01:** Kiến thức cơ bản về EdgeAI và các nghiên cứu thực tế
- **Module02:** Các họ và kiến trúc của Mô hình Ngôn ngữ Nhỏ (SLM)
- **Module03:** Chiến lược triển khai cục bộ và trên đám mây
- **Module04:** Tối ưu hóa mô hình với nhiều framework
- **Module05:** SLMOps - vận hành sản xuất
- **Module06:** Các tác nhân AI và gọi hàm
- **Module07:** Triển khai theo nền tảng cụ thể
- **Module08:** Bộ công cụ Foundry Local với 10 mẫu toàn diện

### Phụ thuộc bên ngoài
- [Microsoft Foundry Local](https://foundry.microsoft.com/) - Runtime mô hình AI cục bộ
- [Llama.cpp](https://github.com/ggml-org/llama.cpp) - Framework tối ưu hóa
- [Microsoft Olive](https://microsoft.github.io/Olive/) - Bộ công cụ tối ưu hóa mô hình
- [OpenVINO](https://docs.openvino.ai/) - Bộ công cụ tối ưu hóa của Intel

## Ghi chú cụ thể về dự án

### Ứng dụng mẫu Module08

Kho bao gồm 10 ứng dụng mẫu toàn diện:

1. **01-REST Chat Quickstart** - Tích hợp cơ bản OpenAI SDK
2. **02-OpenAI SDK Integration** - Các tính năng nâng cao của SDK
3. **03-Model Discovery & Benchmarking** - Công cụ so sánh mô hình
4. **04-Chainlit RAG Application** - Tạo nội dung dựa trên truy xuất
5. **05-Multi-Agent Orchestration** - Điều phối tác nhân cơ bản
6. **06-Models-as-Tools Router** - Định tuyến mô hình thông minh
7. **07-Direct API Client** - Tích hợp API cấp thấp
8. **08-Windows 11 Chat App** - Ứng dụng máy tính để bàn Electron gốc
9. **09-Advanced Multi-Agent System** - Điều phối tác nhân phức tạp
10. **10-Foundry Tools Framework** - Tích hợp LangChain/Semantic Kernel

Mỗi mẫu minh họa các khía cạnh khác nhau của phát triển Edge AI với Foundry Local.

### Cân nhắc về hiệu suất

- SLMs được tối ưu hóa cho triển khai cục bộ (2-16GB RAM)
- Suy luận cục bộ cung cấp thời gian phản hồi 50-500ms
- Kỹ thuật lượng hóa đạt giảm kích thước 75% với giữ lại 85% hiệu suất
- Khả năng hội thoại thời gian thực với các mô hình cục bộ

### Bảo mật và quyền riêng tư

- Tất cả xử lý diễn ra cục bộ - không có dữ liệu gửi lên đám mây
- Phù hợp cho các ứng dụng nhạy cảm về quyền riêng tư (y tế, tài chính)
- Đáp ứng yêu cầu về chủ quyền dữ liệu
- Foundry Local chạy hoàn toàn trên phần cứng cục bộ

---

**Đây là một kho tài liệu giáo dục tập trung vào việc giảng dạy phát triển Edge AI. Mẫu đóng góp chính là cải thiện nội dung giáo dục và thêm/cải thiện các ứng dụng mẫu minh họa các khái niệm Edge AI.**

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với các thông tin quan trọng, khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.