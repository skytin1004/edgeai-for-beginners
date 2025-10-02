<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "65a22ed38b95f334dd8a893bf2c55806",
  "translation_date": "2025-10-02T13:36:43+00:00",
  "source_file": "Module07/aitoolkit.md",
  "language_code": "vi"
}
-->
# Bộ công cụ AI cho Visual Studio Code - Hướng dẫn phát triển AI tại Edge

## Giới thiệu

Chào mừng bạn đến với hướng dẫn toàn diện về cách sử dụng Bộ công cụ AI cho Visual Studio Code trong phát triển AI tại Edge. Khi trí tuệ nhân tạo chuyển từ điện toán đám mây tập trung sang các thiết bị phân tán tại Edge, các nhà phát triển cần những công cụ mạnh mẽ và tích hợp để xử lý các thách thức độc đáo của việc triển khai tại Edge - từ hạn chế tài nguyên đến yêu cầu hoạt động ngoại tuyến.

Bộ công cụ AI cho Visual Studio Code lấp đầy khoảng trống này bằng cách cung cấp một môi trường phát triển hoàn chỉnh, được thiết kế đặc biệt để xây dựng, kiểm thử và tối ưu hóa các ứng dụng AI hoạt động hiệu quả trên các thiết bị Edge. Dù bạn đang phát triển cho cảm biến IoT, thiết bị di động, hệ thống nhúng hay máy chủ Edge, bộ công cụ này sẽ đơn giản hóa toàn bộ quy trình phát triển của bạn trong môi trường quen thuộc của VS Code.

Hướng dẫn này sẽ đưa bạn qua các khái niệm cơ bản, công cụ và các thực tiễn tốt nhất để tận dụng Bộ công cụ AI trong các dự án AI tại Edge của bạn, từ việc chọn mô hình ban đầu đến triển khai sản phẩm.

## Tổng quan

Bộ công cụ AI cho Visual Studio Code là một tiện ích mạnh mẽ giúp đơn giản hóa việc phát triển tác nhân và tạo ứng dụng AI. Bộ công cụ này cung cấp các khả năng toàn diện để khám phá, đánh giá và triển khai các mô hình AI từ nhiều nhà cung cấp—bao gồm Anthropic, OpenAI, GitHub, Google—đồng thời hỗ trợ thực thi mô hình cục bộ bằng ONNX và Ollama.

Điểm nổi bật của Bộ công cụ AI là cách tiếp cận toàn diện đối với toàn bộ vòng đời phát triển AI. Không giống như các công cụ phát triển AI truyền thống chỉ tập trung vào một khía cạnh, Bộ công cụ AI cung cấp một môi trường tích hợp bao gồm khám phá mô hình, thử nghiệm, phát triển tác nhân, đánh giá và triển khai—tất cả trong môi trường quen thuộc của VS Code.

Nền tảng này được thiết kế đặc biệt cho việc tạo mẫu nhanh và triển khai sản phẩm, với các tính năng như tạo gợi ý, khởi động nhanh, tích hợp công cụ MCP (Model Context Protocol) liền mạch, và khả năng đánh giá mở rộng. Đối với phát triển AI tại Edge, điều này có nghĩa là bạn có thể phát triển, kiểm thử và tối ưu hóa các ứng dụng AI một cách hiệu quả cho các kịch bản triển khai tại Edge trong khi vẫn duy trì toàn bộ quy trình phát triển trong VS Code.

## Mục tiêu học tập

Khi hoàn thành hướng dẫn này, bạn sẽ có thể:

### Năng lực cốt lõi
- **Cài đặt và cấu hình** Bộ công cụ AI cho Visual Studio Code để phục vụ quy trình phát triển AI tại Edge
- **Điều hướng và sử dụng** giao diện Bộ công cụ AI, bao gồm Model Catalog, Playground, và Agent Builder
- **Chọn và đánh giá** các mô hình AI phù hợp để triển khai tại Edge dựa trên hiệu suất và hạn chế tài nguyên
- **Chuyển đổi và tối ưu hóa** các mô hình bằng định dạng ONNX và kỹ thuật lượng hóa cho các thiết bị Edge

### Kỹ năng phát triển AI tại Edge
- **Thiết kế và triển khai** các ứng dụng AI tại Edge bằng môi trường phát triển tích hợp
- **Kiểm thử mô hình** trong điều kiện giống Edge bằng cách suy luận cục bộ và giám sát tài nguyên
- **Tạo và tùy chỉnh** các tác nhân AI được tối ưu hóa cho các kịch bản triển khai tại Edge
- **Đánh giá hiệu suất mô hình** bằng các chỉ số liên quan đến điện toán tại Edge (độ trễ, sử dụng bộ nhớ, độ chính xác)

### Tối ưu hóa và triển khai
- **Áp dụng kỹ thuật lượng hóa và cắt tỉa** để giảm kích thước mô hình trong khi vẫn duy trì hiệu suất chấp nhận được
- **Tối ưu hóa mô hình** cho các nền tảng phần cứng Edge cụ thể bao gồm tăng tốc CPU, GPU và NPU
- **Thực hiện các thực tiễn tốt nhất** cho phát triển AI tại Edge bao gồm quản lý tài nguyên và chiến lược dự phòng
- **Chuẩn bị mô hình và ứng dụng** để triển khai sản phẩm trên các thiết bị Edge

### Các khái niệm nâng cao về AI tại Edge
- **Tích hợp với các framework AI tại Edge** bao gồm ONNX Runtime, Windows ML, và TensorFlow Lite
- **Triển khai kiến trúc đa mô hình** và các kịch bản học liên kết cho môi trường Edge
- **Khắc phục các vấn đề phổ biến về AI tại Edge** bao gồm hạn chế bộ nhớ, tốc độ suy luận, và khả năng tương thích phần cứng
- **Thiết kế chiến lược giám sát và ghi nhật ký** cho các ứng dụng AI tại Edge trong môi trường sản xuất

### Ứng dụng thực tiễn
- **Xây dựng giải pháp AI tại Edge từ đầu đến cuối** từ việc chọn mô hình đến triển khai
- **Thể hiện sự thành thạo** trong quy trình phát triển và kỹ thuật tối ưu hóa dành riêng cho Edge
- **Áp dụng các khái niệm đã học** vào các trường hợp sử dụng AI tại Edge thực tế bao gồm IoT, di động, và ứng dụng nhúng
- **Đánh giá và so sánh** các chiến lược triển khai AI tại Edge khác nhau và các đánh đổi của chúng

## Các tính năng chính cho phát triển AI tại Edge

### 1. Danh mục mô hình và khám phá
- **Hỗ trợ đa nhà cung cấp**: Duyệt và truy cập các mô hình AI từ Anthropic, OpenAI, GitHub, Google, và các nhà cung cấp khác
- **Tích hợp mô hình cục bộ**: Khám phá đơn giản các mô hình ONNX và Ollama để triển khai tại Edge
- **Mô hình GitHub**: Tích hợp trực tiếp với lưu trữ mô hình của GitHub để truy cập dễ dàng
- **So sánh mô hình**: So sánh các mô hình cạnh nhau để tìm sự cân bằng tối ưu cho các hạn chế của thiết bị Edge

### 2. Playground tương tác
- **Môi trường thử nghiệm tương tác**: Thử nghiệm nhanh các khả năng của mô hình trong môi trường kiểm soát
- **Hỗ trợ đa phương thức**: Kiểm thử với hình ảnh, văn bản, và các đầu vào khác thường gặp trong các kịch bản tại Edge
- **Thử nghiệm thời gian thực**: Phản hồi ngay lập tức về các phản hồi và hiệu suất của mô hình
- **Tối ưu hóa tham số**: Tinh chỉnh các tham số mô hình cho các yêu cầu triển khai tại Edge

### 3. Trình tạo gợi ý (Agent Builder)
- **Tạo ngôn ngữ tự nhiên**: Tạo gợi ý khởi đầu bằng các mô tả ngôn ngữ tự nhiên
- **Tinh chỉnh lặp lại**: Cải thiện gợi ý dựa trên phản hồi và hiệu suất của mô hình
- **Phân chia nhiệm vụ**: Phân chia các nhiệm vụ phức tạp bằng cách xâu chuỗi gợi ý và đầu ra có cấu trúc
- **Hỗ trợ biến**: Sử dụng biến trong gợi ý để tạo hành vi tác nhân động
- **Tạo mã sản xuất**: Tạo mã sẵn sàng cho sản xuất để phát triển ứng dụng nhanh chóng

### 4. Chạy hàng loạt và đánh giá
- **Kiểm thử đa mô hình**: Thực hiện nhiều gợi ý trên các mô hình đã chọn đồng thời
- **Kiểm thử hiệu quả ở quy mô lớn**: Kiểm thử các đầu vào và cấu hình khác nhau một cách hiệu quả
- **Trường hợp kiểm thử tùy chỉnh**: Chạy các tác nhân với các trường hợp kiểm thử để xác thực chức năng
- **So sánh hiệu suất**: So sánh kết quả trên các mô hình và cấu hình khác nhau

### 5. Đánh giá mô hình với tập dữ liệu
- **Chỉ số tiêu chuẩn**: Kiểm thử các mô hình AI bằng các bộ đánh giá tích hợp (F1 score, độ liên quan, độ tương đồng, độ mạch lạc)
- **Bộ đánh giá tùy chỉnh**: Tạo các chỉ số đánh giá riêng cho các trường hợp sử dụng cụ thể
- **Tích hợp tập dữ liệu**: Kiểm thử mô hình với các tập dữ liệu toàn diện
- **Đo lường hiệu suất**: Định lượng hiệu suất mô hình để đưa ra quyết định triển khai tại Edge

### 6. Khả năng tinh chỉnh
- **Tùy chỉnh mô hình**: Tùy chỉnh mô hình cho các trường hợp sử dụng và lĩnh vực cụ thể
- **Thích nghi chuyên biệt**: Thích nghi mô hình với các yêu cầu và lĩnh vực chuyên biệt
- **Tối ưu hóa tại Edge**: Tinh chỉnh mô hình đặc biệt cho các hạn chế triển khai tại Edge
- **Đào tạo theo lĩnh vực**: Tạo các mô hình phù hợp với các trường hợp sử dụng tại Edge cụ thể

### 7. Tích hợp công cụ MCP
- **Kết nối công cụ bên ngoài**: Kết nối các tác nhân với các công cụ bên ngoài thông qua các máy chủ Model Context Protocol
- **Hành động thực tế**: Cho phép các tác nhân truy vấn cơ sở dữ liệu, truy cập API, hoặc thực thi logic tùy chỉnh
- **Máy chủ MCP hiện có**: Sử dụng các công cụ từ giao thức lệnh (stdio) hoặc HTTP (sự kiện gửi từ máy chủ)
- **Phát triển MCP tùy chỉnh**: Xây dựng và tạo khung các máy chủ MCP mới với kiểm thử trong Agent Builder

### 8. Phát triển và kiểm thử tác nhân
- **Hỗ trợ gọi hàm**: Cho phép các tác nhân gọi các hàm bên ngoài một cách động
- **Kiểm thử tích hợp thời gian thực**: Kiểm thử tích hợp với các lần chạy thời gian thực và sử dụng công cụ
- **Phiên bản hóa tác nhân**: Quản lý phiên bản cho các tác nhân với khả năng so sánh kết quả đánh giá
- **Gỡ lỗi và truy vết**: Khả năng truy vết và gỡ lỗi cục bộ cho phát triển tác nhân

## Quy trình phát triển AI tại Edge

### Giai đoạn 1: Khám phá và chọn mô hình
1. **Khám phá Danh mục Mô hình**: Sử dụng danh mục mô hình để tìm các mô hình phù hợp cho triển khai tại Edge
2. **So sánh hiệu suất**: Đánh giá các mô hình dựa trên kích thước, độ chính xác, và tốc độ suy luận
3. **Kiểm thử cục bộ**: Sử dụng các mô hình Ollama hoặc ONNX để kiểm thử cục bộ trước khi triển khai tại Edge
4. **Đánh giá yêu cầu tài nguyên**: Xác định nhu cầu bộ nhớ và tính toán cho các thiết bị Edge mục tiêu

### Giai đoạn 2: Tối ưu hóa mô hình
1. **Chuyển đổi sang ONNX**: Chuyển đổi các mô hình đã chọn sang định dạng ONNX để tương thích với Edge
2. **Áp dụng lượng hóa**: Giảm kích thước mô hình thông qua lượng hóa INT8 hoặc INT4
3. **Tối ưu hóa phần cứng**: Tối ưu hóa cho phần cứng Edge mục tiêu (ARM, x86, bộ tăng tốc chuyên dụng)
4. **Xác thực hiệu suất**: Xác thực rằng các mô hình được tối ưu hóa vẫn duy trì độ chính xác chấp nhận được

### Giai đoạn 3: Phát triển ứng dụng
1. **Thiết kế tác nhân**: Sử dụng Agent Builder để tạo các tác nhân AI được tối ưu hóa cho Edge
2. **Kỹ thuật gợi ý**: Phát triển các gợi ý hoạt động hiệu quả với các mô hình Edge nhỏ hơn
3. **Kiểm thử tích hợp**: Kiểm thử các tác nhân trong điều kiện mô phỏng Edge
4. **Tạo mã**: Tạo mã sản xuất được tối ưu hóa cho triển khai tại Edge

### Giai đoạn 4: Đánh giá và kiểm thử
1. **Đánh giá hàng loạt**: Kiểm thử nhiều cấu hình để tìm các thiết lập tối ưu cho Edge
2. **Phân tích hiệu suất**: Phân tích tốc độ suy luận, sử dụng bộ nhớ, và độ chính xác
3. **Mô phỏng Edge**: Kiểm thử trong các điều kiện tương tự môi trường triển khai tại Edge
4. **Kiểm thử áp lực**: Đánh giá hiệu suất dưới các điều kiện tải khác nhau

### Giai đoạn 5: Chuẩn bị triển khai
1. **Tối ưu hóa cuối cùng**: Áp dụng các tối ưu hóa cuối cùng dựa trên kết quả kiểm thử
2. **Đóng gói triển khai**: Đóng gói mô hình và mã để triển khai tại Edge
3. **Tài liệu hóa**: Tài liệu hóa các yêu cầu và cấu hình triển khai
4. **Thiết lập giám sát**: Chuẩn bị giám sát và ghi nhật ký cho triển khai tại Edge

## Đối tượng mục tiêu cho phát triển AI tại Edge

### Các nhà phát triển AI tại Edge
- Các nhà phát triển ứng dụng xây dựng các thiết bị Edge và giải pháp IoT tích hợp AI
- Các nhà phát triển hệ thống nhúng tích hợp khả năng AI vào các thiết bị hạn chế tài nguyên
- Các nhà phát triển di động tạo ứng dụng AI trên thiết bị cho điện thoại thông minh và máy tính bảng

### Kỹ sư AI tại Edge
- Các kỹ sư AI tối ưu hóa mô hình cho triển khai tại Edge và quản lý các pipeline suy luận
- Các kỹ sư DevOps triển khai và quản lý các mô hình AI trên cơ sở hạ tầng Edge phân tán
- Các kỹ sư hiệu suất tối ưu hóa khối lượng công việc AI cho các hạn chế phần cứng tại Edge

### Các nhà nghiên cứu và giáo dục
- Các nhà nghiên cứu AI phát triển các mô hình và thuật toán hiệu quả cho điện toán tại Edge
- Các nhà giáo dục giảng dạy các khái niệm AI tại Edge và trình diễn các kỹ thuật tối ưu hóa
- Sinh viên học về các thách thức và giải pháp trong triển khai AI tại Edge

## Các trường hợp sử dụng AI tại Edge

### Thiết bị IoT thông minh
- **Nhận diện hình ảnh thời gian thực**: Triển khai các mô hình thị giác máy tính trên camera và cảm biến IoT
- **Xử lý giọng nói**: Thực hiện nhận diện giọng nói và xử lý ngôn ngữ tự nhiên trên loa thông minh
- **Bảo trì dự đoán**: Chạy các mô hình phát hiện bất thường trên các thiết bị công nghiệp tại Edge
- **Giám sát môi trường**: Triển khai các mô hình phân tích dữ liệu cảm biến cho các ứng dụng môi trường

### Ứng dụng di động và nhúng
- **Dịch thuật trên thiết bị**: Thực hiện các mô hình dịch ngôn ngữ hoạt động ngoại tuyến
- **Thực tế tăng cường**: Triển khai nhận diện và theo dõi đối tượng thời gian thực cho các ứng dụng AR
- **Giám sát sức khỏe**: Chạy các mô hình phân tích sức khỏe trên thiết bị đeo và thiết bị y tế
- **Hệ thống tự động**: Thực hiện các mô hình ra quyết định cho drone, robot, và phương tiện

### Cơ sở hạ tầng điện toán tại Edge
- **Trung tâm dữ liệu Edge**: Triển khai các mô hình AI trong các trung tâm dữ liệu Edge cho các ứng dụng độ trễ thấp
- **Tích hợp CDN**: Tích hợp khả năng xử lý AI vào các mạng phân phối nội dung
- **Edge 5G**: Tận dụng điện toán Edge 5G cho các ứng dụng hỗ trợ AI
- **Điện toán Fog**: Thực hiện xử lý AI trong các môi trường điện toán Fog

## Cài đặt và thiết lập

### Cài đặt tiện ích
Cài đặt tiện ích Bộ công cụ AI trực tiếp từ Visual Studio Code Marketplace:

**ID tiện ích**: `ms-windows-ai-studio.windows-ai-studio`

**Phương pháp cài đặt**:
1. **VS Code Marketplace**: Tìm kiếm "AI Toolkit" trong mục Extensions
2. **Dòng lệnh**: `code --install-extension ms-windows-ai-studio.windows-ai-studio`
3. **Cài đặt trực tiếp**: Tải xuống từ [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)

### Yêu cầu trước cho phát triển AI tại Edge
- **Visual Studio Code**: Khuyến nghị phiên bản mới nhất
- **Môi trường Python**: Python 3.8+ với các thư viện AI cần thiết
- **ONNX Runtime** (Tùy chọn): Để suy luận mô hình ONNX
- **Ollama** (Tùy chọn): Để phục vụ mô hình cục bộ
- **Công cụ tăng tốc phần cứng**: CUDA, OpenVINO, hoặc các bộ tăng tốc cụ thể theo nền tảng

### Cấu hình ban đầu
1. **Kích hoạt tiện ích**: Mở VS Code và xác minh rằng Bộ công cụ AI xuất hiện trong Activity Bar
2. **Thiết lập nhà cung cấp mô hình**: Cấu hình truy cập vào GitHub, OpenAI, Anthropic, hoặc các nhà cung cấp mô hình khác
3. **Môi trường cục bộ**: Thiết lập môi trường Python và cài đặt các gói cần thiết
4. **Tăng tốc phần cứng**: Cấu hình tăng tốc GPU/NPU nếu có
5. **Tích hợp MCP**: Thiết lập các máy chủ Model Context Protocol nếu cần

### Danh sách kiểm tra thiết lập lần đầu
- [ ] Tiện ích Bộ công cụ AI đã được cài đặt và kích hoạt
- [ ] Danh mục mô hình có thể truy cập và các mô hình có thể khám phá
- [ ] Playground hoạt động để kiểm thử mô hình
- [ ] Agent Builder có thể truy cập để phát triển gợi ý
- [ ] Môi trường phát triển
2. Tạo các gợi ý ban đầu bằng cách sử dụng mô tả ngôn ngữ tự nhiên  
3. Lặp lại và tinh chỉnh các gợi ý dựa trên phản hồi của mô hình  
4. Tích hợp các công cụ MCP để nâng cao khả năng của tác nhân  

#### Bước 3: Kiểm tra và Đánh giá  
1. Sử dụng **Bulk Run** để kiểm tra nhiều gợi ý trên các mô hình đã chọn  
2. Chạy các tác nhân với các trường hợp kiểm tra để xác thực chức năng  
3. Đánh giá độ chính xác và hiệu suất bằng cách sử dụng các chỉ số tích hợp hoặc tùy chỉnh  
4. So sánh các mô hình và cấu hình khác nhau  

#### Bước 4: Tinh chỉnh và Tối ưu hóa  
1. Tùy chỉnh mô hình cho các trường hợp sử dụng đặc biệt  
2. Áp dụng tinh chỉnh theo lĩnh vực cụ thể  
3. Tối ưu hóa cho các hạn chế triển khai tại thiết bị biên  
4. Phiên bản hóa và so sánh các cấu hình tác nhân khác nhau  

#### Bước 5: Chuẩn bị Triển khai  
1. Tạo mã sẵn sàng cho sản xuất bằng Agent Builder  
2. Thiết lập kết nối máy chủ MCP để sử dụng trong sản xuất  
3. Chuẩn bị các gói triển khai cho thiết bị biên  
4. Cấu hình các chỉ số giám sát và đánh giá  

## Các Thực Tiễn Tốt Nhất cho Phát Triển AI tại Thiết Bị Biên  

### Lựa chọn Mô hình  
- **Hạn chế Kích thước**: Chọn các mô hình phù hợp với giới hạn bộ nhớ của thiết bị mục tiêu  
- **Tốc độ Suy luận**: Ưu tiên các mô hình có thời gian suy luận nhanh cho ứng dụng thời gian thực  
- **Cân nhắc Độ chính xác**: Cân bằng giữa độ chính xác của mô hình và các hạn chế về tài nguyên  
- **Tương thích Định dạng**: Ưu tiên định dạng ONNX hoặc tối ưu hóa phần cứng cho triển khai tại thiết bị biên  

### Kỹ thuật Tối ưu hóa  
- **Lượng hóa**: Sử dụng lượng hóa INT8 hoặc INT4 để giảm kích thước mô hình và cải thiện tốc độ  
- **Cắt tỉa**: Loại bỏ các tham số mô hình không cần thiết để giảm yêu cầu tính toán  
- **Chưng cất Kiến thức**: Tạo các mô hình nhỏ hơn nhưng vẫn duy trì hiệu suất của mô hình lớn  
- **Tăng tốc Phần cứng**: Tận dụng NPUs, GPUs hoặc các bộ tăng tốc chuyên dụng khi có  

### Quy trình Phát triển  
- **Kiểm tra Lặp lại**: Kiểm tra thường xuyên trong điều kiện giống thiết bị biên trong quá trình phát triển  
- **Giám sát Hiệu suất**: Liên tục giám sát việc sử dụng tài nguyên và tốc độ suy luận  
- **Quản lý Phiên bản**: Theo dõi các phiên bản mô hình và cài đặt tối ưu hóa  
- **Tài liệu hóa**: Ghi lại tất cả các quyết định tối ưu hóa và các cân nhắc về hiệu suất  

### Cân nhắc Triển khai  
- **Giám sát Tài nguyên**: Giám sát bộ nhớ, CPU và mức tiêu thụ năng lượng trong sản xuất  
- **Chiến lược Dự phòng**: Triển khai các cơ chế dự phòng cho các lỗi mô hình  
- **Cơ chế Cập nhật**: Lên kế hoạch cho các bản cập nhật mô hình và quản lý phiên bản  
- **Bảo mật**: Áp dụng các biện pháp bảo mật phù hợp cho các ứng dụng AI tại thiết bị biên  

## Tích hợp với Các Khung AI tại Thiết Bị Biên  

### ONNX Runtime  
- **Triển khai Đa nền tảng**: Triển khai các mô hình ONNX trên các nền tảng thiết bị biên khác nhau  
- **Tối ưu hóa Phần cứng**: Tận dụng các tối ưu hóa phần cứng cụ thể của ONNX Runtime  
- **Hỗ trợ Di động**: Sử dụng ONNX Runtime Mobile cho các ứng dụng trên điện thoại thông minh và máy tính bảng  
- **Tích hợp IoT**: Triển khai trên các thiết bị IoT bằng các phiên bản nhẹ của ONNX Runtime  

### Windows ML  
- **Thiết bị Windows**: Tối ưu hóa cho các thiết bị biên và PC chạy Windows  
- **Tăng tốc NPU**: Tận dụng các Neural Processing Units trên thiết bị Windows  
- **DirectML**: Sử dụng DirectML để tăng tốc GPU trên các nền tảng Windows  
- **Tích hợp UWP**: Tích hợp với các ứng dụng Universal Windows Platform  

### TensorFlow Lite  
- **Tối ưu hóa Di động**: Triển khai các mô hình TensorFlow Lite trên các thiết bị di động và nhúng  
- **Đại diện Phần cứng**: Sử dụng các đại diện phần cứng chuyên dụng để tăng tốc  
- **Vi điều khiển**: Triển khai trên các vi điều khiển bằng TensorFlow Lite Micro  
- **Hỗ trợ Đa nền tảng**: Triển khai trên Android, iOS và các hệ thống Linux nhúng  

### Azure IoT Edge  
- **Kết hợp Cloud-Biên**: Kết hợp huấn luyện trên đám mây với suy luận tại thiết bị biên  
- **Triển khai Module**: Triển khai các mô hình AI dưới dạng module IoT Edge  
- **Quản lý Thiết bị**: Quản lý thiết bị biên và cập nhật mô hình từ xa  
- **Thu thập Dữ liệu**: Thu thập dữ liệu hiệu suất và các chỉ số mô hình từ các triển khai tại thiết bị biên  

## Các Kịch bản AI tại Thiết Bị Biên Nâng cao  

### Triển khai Đa mô hình  
- **Tập hợp Mô hình**: Triển khai nhiều mô hình để cải thiện độ chính xác hoặc tính dự phòng  
- **Kiểm tra A/B**: Kiểm tra đồng thời các mô hình khác nhau trên thiết bị biên  
- **Lựa chọn Động**: Chọn mô hình dựa trên điều kiện hiện tại của thiết bị  
- **Chia sẻ Tài nguyên**: Tối ưu hóa việc sử dụng tài nguyên giữa các mô hình được triển khai  

### Học Liên kết  
- **Huấn luyện Phân tán**: Huấn luyện mô hình trên nhiều thiết bị biên  
- **Bảo vệ Quyền riêng tư**: Giữ dữ liệu huấn luyện tại chỗ trong khi chia sẻ cải tiến mô hình  
- **Học Tập Hợp tác**: Cho phép các thiết bị học hỏi từ kinh nghiệm chung  
- **Phối hợp Biên-Đám mây**: Phối hợp học tập giữa các thiết bị biên và hạ tầng đám mây  

### Xử lý Thời gian thực  
- **Xử lý Dòng**: Xử lý các luồng dữ liệu liên tục trên thiết bị biên  
- **Suy luận Độ trễ thấp**: Tối ưu hóa để giảm thiểu độ trễ suy luận  
- **Xử lý Theo Lô**: Xử lý hiệu quả các lô dữ liệu trên thiết bị biên  
- **Xử lý Thích ứng**: Điều chỉnh xử lý dựa trên khả năng hiện tại của thiết bị  

## Khắc phục sự cố Phát triển AI tại Thiết Bị Biên  

### Các Vấn đề Thường gặp  
- **Hạn chế Bộ nhớ**: Mô hình quá lớn so với bộ nhớ của thiết bị mục tiêu  
- **Tốc độ Suy luận**: Suy luận mô hình quá chậm so với yêu cầu thời gian thực  
- **Suy giảm Độ chính xác**: Tối ưu hóa làm giảm độ chính xác của mô hình không chấp nhận được  
- **Tương thích Phần cứng**: Mô hình không tương thích với phần cứng mục tiêu  

### Chiến lược Gỡ lỗi  
- **Phân tích Hiệu suất**: Sử dụng các tính năng theo dõi của AI Toolkit để xác định các điểm nghẽn  
- **Giám sát Tài nguyên**: Giám sát việc sử dụng bộ nhớ và CPU trong quá trình phát triển  
- **Kiểm tra Từng bước**: Kiểm tra các tối ưu hóa từng bước để cô lập vấn đề  
- **Mô phỏng Phần cứng**: Sử dụng các công cụ phát triển để mô phỏng phần cứng mục tiêu  

### Giải pháp Tối ưu hóa  
- **Lượng hóa Thêm**: Áp dụng các kỹ thuật lượng hóa mạnh mẽ hơn  
- **Kiến trúc Mô hình**: Xem xét các kiến trúc mô hình khác được tối ưu hóa cho thiết bị biên  
- **Tối ưu hóa Tiền xử lý**: Tối ưu hóa việc tiền xử lý dữ liệu cho các hạn chế tại thiết bị biên  
- **Tối ưu hóa Suy luận**: Sử dụng các tối ưu hóa suy luận cụ thể cho phần cứng  

## Tài nguyên và Các bước Tiếp theo  

### Tài liệu Chính thức  
- [Tài liệu Nhà phát triển AI Toolkit](https://aka.ms/AIToolkit/doc)  
- [Hướng dẫn Cài đặt và Thiết lập](https://code.visualstudio.com/docs/intelligentapps/overview#_install-and-setup)  
- [Tài liệu Ứng dụng Thông minh VS Code](https://code.visualstudio.com/docs/intelligentapps)  
- [Tài liệu Model Context Protocol (MCP)](https://modelcontextprotocol.io/)  

### Cộng đồng và Hỗ trợ  
- [Kho GitHub AI Toolkit](https://github.com/microsoft/vscode-ai-toolkit)  
- [Vấn đề và Yêu cầu Tính năng trên GitHub](https://aka.ms/AIToolkit/feedback)  
- [Cộng đồng Discord Azure AI Foundry](https://aka.ms/azureaifoundry/discord)  
- [Chợ Tiện ích Mở rộng VS Code](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)  

### Tài nguyên Kỹ thuật  
- [Tài liệu ONNX Runtime](https://onnxruntime.ai/)  
- [Tài liệu Ollama](https://ollama.ai/)  
- [Tài liệu Windows ML](https://docs.microsoft.com/en-us/windows/ai/)  
- [Tài liệu Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/)  

### Lộ trình Học tập  
- [Khóa học Cơ bản về AI tại Thiết bị Biên](../Module01/README.md)  
- [Hướng dẫn về Mô hình Ngôn ngữ Nhỏ](../Module02/README.md)  
- [Chiến lược Triển khai tại Thiết bị Biên](../Module03/README.md)  
- [Phát triển AI tại Thiết bị Biên trên Windows](./windowdeveloper.md)  

### Tài nguyên Bổ sung  
- **Thống kê Kho**: Hơn 1.8k sao, hơn 150 nhánh, hơn 18 người đóng góp  
- **Giấy phép**: Giấy phép MIT  
- **Bảo mật**: Áp dụng các chính sách bảo mật của Microsoft  
- **Thu thập Dữ liệu**: Tôn trọng cài đặt thu thập dữ liệu của VS Code  

## Kết luận  

AI Toolkit cho Visual Studio Code là một nền tảng toàn diện cho phát triển AI hiện đại, cung cấp các khả năng phát triển tác nhân được tối ưu hóa đặc biệt cho các ứng dụng AI tại thiết bị biên. Với danh mục mô hình phong phú hỗ trợ các nhà cung cấp như Anthropic, OpenAI, GitHub, và Google, kết hợp với khả năng thực thi cục bộ thông qua ONNX và Ollama, bộ công cụ này mang lại sự linh hoạt cần thiết cho các kịch bản triển khai tại thiết bị biên đa dạng.

Điểm mạnh của bộ công cụ nằm ở cách tiếp cận tích hợp—từ việc khám phá và thử nghiệm mô hình trong Playground đến phát triển tác nhân tinh vi với Prompt Builder, khả năng đánh giá toàn diện, và tích hợp công cụ MCP liền mạch. Đối với các nhà phát triển AI tại thiết bị biên, điều này có nghĩa là tạo mẫu nhanh và kiểm tra các tác nhân AI trước khi triển khai, với khả năng lặp lại nhanh chóng và tối ưu hóa cho các môi trường hạn chế tài nguyên.

Các lợi ích chính cho phát triển AI tại thiết bị biên bao gồm:  
- **Thử nghiệm Nhanh**: Kiểm tra mô hình và tác nhân nhanh chóng trước khi triển khai tại thiết bị biên  
- **Linh hoạt Đa nhà cung cấp**: Truy cập các mô hình từ nhiều nguồn để tìm giải pháp tối ưu cho thiết bị biên  
- **Phát triển Cục bộ**: Kiểm tra với ONNX và Ollama để phát triển ngoại tuyến và bảo vệ quyền riêng tư  
- **Sẵn sàng Sản xuất**: Tạo mã sẵn sàng cho sản xuất và tích hợp với các công cụ bên ngoài qua MCP  
- **Đánh giá Toàn diện**: Sử dụng các chỉ số tích hợp và tùy chỉnh để xác thực hiệu suất AI tại thiết bị biên  

Khi AI tiếp tục hướng tới các kịch bản triển khai tại thiết bị biên, AI Toolkit cho VS Code cung cấp môi trường phát triển và quy trình làm việc cần thiết để xây dựng, kiểm tra, và tối ưu hóa các ứng dụng thông minh cho các môi trường hạn chế tài nguyên. Dù bạn đang phát triển các giải pháp IoT, ứng dụng AI di động, hay hệ thống trí tuệ nhúng, bộ công cụ này với bộ tính năng toàn diện và quy trình làm việc tích hợp hỗ trợ toàn bộ vòng đời phát triển AI tại thiết bị biên.

Với sự phát triển liên tục và cộng đồng tích cực (hơn 1.8k sao trên GitHub), AI Toolkit vẫn dẫn đầu trong các công cụ phát triển AI, không ngừng tiến hóa để đáp ứng nhu cầu của các nhà phát triển AI hiện đại xây dựng cho các kịch bản triển khai tại thiết bị biên.

[Next Foundry Local](./foundrylocal.md)

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với thông tin quan trọng, khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.