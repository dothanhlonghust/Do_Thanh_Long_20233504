# Truong huu han GF(2^8) voi da thuc toi gian chuan AES:
# p(x) = x^8 + x^4 + x^3 + x + 1 (ma hex: 0x11B)

def phep_xor(a, b):
    return a ^ b

def nhan_voi_x_gf8(g):
    # Kiem tra bit cao nhat (bit 7) xem co bi tran khoi 8-bit khong
    bit_cao_nhat = (g >> 7) & 1
    ket_qua = (g << 1) & 0xFF
    if bit_cao_nhat == 1:
        # Neu tran, XOR voi 0x1B (phan du sau khi bo bit x^8)
        ket_qua = phep_xor(ket_qua, 0x1B)
    return ket_qua

def multiply_gf2m8(f, g):
    ket_qua = 0
    temp = g
    for i in range(8):
        bit = (f >> i) & 1
        if bit == 1:
            ket_qua = phep_xor(ket_qua, temp)
        temp = nhan_voi_x_gf8(temp)
    return ket_qua

if __name__ == "__main__":
    # Test thu theo cap gia tri chuan trong tieu chuan AES
    # 0x57 * 0x83 = 0xc1
    a = 0x57
    b = 0x83
    kq = multiply_gf2m8(a, b)
    print(f"Ket qua {hex(a)} * {hex(b)} trong GF(2^8) = {hex(kq)}")