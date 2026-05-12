## Mô tả các file

### `Liên kết dữ liệu.txt`
- Chứa link dẫn đến các folder chứa dữ lieu
- Lưu ý: Các file code được lập trình để chạy được trên Colab Research Google nên khi muốn chạy code, cần tạo lối tắt tất cả các folder vào mục My Drive trên Drive Google

### `demo.zip`
- Chứa các file code được dùng để chạy demo trang web, vui lòng đọc theo hướng dẫn trong file demo/readme.txt để có thể thực thi

### `Baseline_Model.ipynb`
- Mô hình baseline dựa trên **độ phổ biến (popularity)**.
- Gợi ý Top-N bài hát có số lượt nghe cao nhất.

### `Collaborative_Filtering.ipynb`
- Huấn luyện và so sánh 3 mô hình CF:
  - User-based
  - Item-based
  - ALS

### `Data_Merge_(user_behavior).ipynb`
- Hợp nhất dữ liệu người dùng và bài hát.
- Bao gồm: audio features, người dùng, lượt nghe và lời bài hát.

### `Exploratory_Data_Analysis.ipynb`
- Khai phá và phân tích dữ liệu (EDA).
- Chỉ tập trung tìm hiểu dữ liệu, **chưa tiền xử lý**.

### `Late_Fusion_Content_based_System.ipynb`
- Hệ thống gợi ý **Content-based** sử dụng Late Fusion.
- Kết hợp audio features và lyrics.

### `Hybrid.ipynb`
- Mô hình **Hybrid Recommendation System**.
- Kết hợp Collaborative Filtering và Content-based.