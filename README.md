# Triển khai thuật toán nhân trong trường hữu hạn Galois Field

Bài tập lớn / bài thực hành triển khai phép nhân trong trường Galois:
- **GF(2^4)**: Sử dụng đa thức tối giản $p(x) = x^4 + x + 1$ (`0x13`).
- **GF(2^8)**: Sử dụng đa thức tối giản chuẩn AES $p(x) = x^8 + x^4 + x^3 + x + 1$ (`0x11B`).

## Cấu trúc thư mục
- `gf2m4.py`: Thuật toán nhân trong trường $GF(2^4)$.
- `gf2m8.py`: Thuật toán nhân trong trường $GF(2^8)$.
- `main.py`: Giao diện dòng lệnh (CLI) điều hướng chương trình.

## Hướng dẫn sử dụng
Chạy tệp chính để sử dụng menu:
```bash
python main.py