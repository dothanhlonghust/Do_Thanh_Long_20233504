# Truong huu han GF(2^4) voi da thuc toi gian p(x) = x^4 + x + 1 (0x13)
# Chuyen doi tu thuat toan C++ sang Python

def phep_xor(a, b):
    return a ^ b

def nhan_voi_x(g):
    # Kiem tra bit cao nhat (bit 3) truoc khi dich
    bit_cao_nhat = (g >> 3) & 1
    ket_qua = (g << 1) & 0x0F
    if bit_cao_nhat == 1:
        ket_qua = phep_xor(ket_qua, 0x03)  # x^4 = x + 1 (0b0011 = 0x03)
    return ket_qua

def multiply_gf2m4(f, g):
    ket_qua = 0
    temp = g
    for i in range(4):
        bit = (f >> i) & 1
        if bit == 1:
            ket_qua = phep_xor(ket_qua, temp)
        temp = nhan_voi_x(temp)
    return ket_qua

if __name__ == "__main__":
    # Test thu mot so phep nhan co ban
    a = 8
    b = 4
    kq = multiply_gf2m4(a, b)
    print(f"Ket qua {a} * {b} trong GF(2^4) = {kq} (Hex: {hex(kq)})")