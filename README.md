<h2 align="center">
    <a href="https://dainam.edu.vn/vi/khoa-cong-nghe-thong-tin">
    🎓  FACULTY OF INFORMATION TECHNOLOGY (DAINAM UNIVERSITY)
    </a>
</h2>
<h2 align="center">
    PHÂN LOẠI BỆNH TRÊN THÂN LÁ LÚA BẰNG CÁC PHƯƠNG PHÁP HỌC SÂU
</h2>

<div align="center">
    <p align="center">
        <img src="docs/aiotlab_logo.png" alt="AIoTLab Logo" width="170"/>
        <img src="docs/fitdnu_logo.png" alt="FIT DNU Logo" width="180"/>
        <img src="docs/dnu_logo.png" alt="DaiNam University Logo" width="200"/>
    </p>

[![AIoTLab](https://img.shields.io/badge/AIoTLab-green?style=for-the-badge)](https://www.facebook.com/DNUAIoTLab)
[![Faculty of Information Technology](https://img.shields.io/badge/Faculty%20of%20Information%20Technology-blue?style=for-the-badge)](https://dainam.edu.vn/vi/khoa-cong-nghe-thong-tin)
[![DaiNam University](https://img.shields.io/badge/DaiNam%20University-orange?style=for-the-badge)](https://dainam.edu.vn)

</div>

---

## 📖 1. Giới thiệu dự án
Dự án "Rice Leaf Disease Classifier" là một bộ mã nguồn dùng để huấn luyện, đánh giá và suy luận mô hình học sâu nhằm phát hiện một số bệnh phổ biến trên lá lúa (ví dụ: Bacterialblight, Blast, Brownspot, Tungro). Mục tiêu là cung cấp tài nguyên để bạn thử nghiệm inference bằng mô hình đã huấn luyện và khám phá pipeline tiền xử lý/huấn luyện trong notebook.

✨ Nội dung chính trong repo:
- Mã nguồn và notebook: `app.py`, `test.py`, `Rice Leaf Disease Classifier.ipynb`, `test.ipynb`.
- Mô hình huấn luyện sẵn: trong thư mục `Model/` (ví dụ `best_model.h5`, `best_model.keras`, `best_model.onnx`).
- Bộ ảnh mẫu và dữ liệu: `Rice Leaf Disease Images/`, `rice leaf diseases dataset/`.

---

## 🔧 2. Yêu cầu & cài đặt
1. Cài Python 3.8+.
2. Tạo và kích hoạt virtual environment, sau đó cài các phụ thuộc:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Ghi chú: Nếu PowerShell chặn script khi kích hoạt venv, chạy `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned` với quyền admin hoặc dùng Command Prompt để activate.

---

## 📁 3. Cấu trúc thư mục
- `app.py` —  entry-point cho ứng dụng/giao diện hoặc API inference.
- `test.py` — script mẫu để chạy dự đoán trên 1 ảnh hoặc thư mục.
- `Rice Leaf Disease Classifier.ipynb` / `test.ipynb` — notebook minh họa tiền xử lý, huấn luyện và đánh giá.
- `requirements.txt` — thư viện cần cài.
- `Model/` — chứa các mô hình đã huấn luyện.
- `Rice Leaf Disease Images/`, `rice leaf diseases dataset/` — ảnh dữ liệu chia theo nhãn.
- link data : https://drive.google.com/drive/folders/1V23bsm3YxLixJh39kGToP1n8EkNXG9bZ?usp=sharing
---

## 🚀 4. Hướng dẫn chạy

1) Chạy inference với `test.py` (ví dụ):

```powershell
\.venv\Scripts\Activate.ps1
python test.py --image "Rice Leaf Disease Images\example.jpg"
```

Script thường sẽ load mô hình từ `Model/` và in ra nhãn dự đoán cùng xác suất.

2) Mở notebook để chạy tương tác:

```powershell
\.venv\Scripts\Activate.ps1
jupyter notebook "Rice Leaf Disease Classifier.ipynb"
```

3) Nếu dự án có `app.py` để chạy giao diện/web:

```powershell
\.venv\Scripts\Activate.ps1
python app.py
```

Kiểm tra nội dung file để biết port/endpoint nếu là web app.

---

## 🧾 5. Mô tả các file chính
- `Model/best_model.h5` / `best_model.keras` / `best_model.onnx`: các định dạng mô hình bạn có thể dùng để inference.
- `test.py`: ví dụ load model và chạy dự đoán.
- `Rice Leaf Disease Classifier.ipynb`: hướng dẫn từng bước tiền xử lý, augmentation (nếu có) và đánh giá.
- `app.py`: (nếu có) chứa mã khởi chạy dịch vụ hoặc giao diện.

---

## ⚠️ Ghi chú
- Đảm bảo versions của `tensorflow`/`torch` tương thích với môi trường (và CUDA nếu dùng GPU).
- Tiền xử lý ảnh (resize, chuẩn hóa) cần trùng với pipeline lúc huấn luyện; kiểm tra trong `test.py`/notebook.
- Nếu cần chuyển đổi định dạng mô hình (ví dụ `.h5` → `.onnx`), kiểm tra thư mục `Model/` để xem ví dụ mẫu.

---

## ✅ Bắt đầu nhanh
- Chạy `test.py` trên ảnh mẫu trong `Rice Leaf Disease Images/`.
- Mở notebook để xem pipeline chi tiết và thử huấn luyện lại nếu cần.

---


---

## ✉️ 5. Liên hệ cá nhân
Nếu bạn cần trao đổi thêm hoặc muốn phát triển mở rộng hệ thống, vui lòng liên hệ:  

- 👨‍💻 Tác giả: Đào Duy Mạnh
- 📧 Email: Manh12088@gmail.com
- 🏫 Lớp: CNTT 16-04
- 🏢 Khoa: Công nghệ thông tin – Trường Đại học Đại Nam
- 🌐 GitHub: github.com/DaoDuyManh
