import sys
from gf2m4 import multiply_gf2m4
from gf2m8 import multiply_gf2m8

def menu_gf2m4():
    print("\n--- NHAN TRONG TRUONG GF(2^4) ---")
    print("Da thuc toi gian: p(x) = x^4 + x + 1 (0x13)")
    try:
        a_str = input("Nhap he so thu nhat a (0-15 hoac hex 0x...): ").strip()
        b_str = input("Nhap he so thu hai b (0-15 hoac hex 0x...): ").strip()
        a = int(a_str, 0)
        b = int(b_str, 0)
        
        if not (0 <= a <= 15 and 0 <= b <= 15):
            print("Loi: Gia tri phai nam trong khoang [0, 15] cua GF(2^4)!")
            return
            
        kq = multiply_gf2m4(a, b)
        print(f"-> Ket qua: {a} * {b} = {kq} (Hex: {hex(kq)}, Bin: {bin(kq)})")
    except ValueError:
        print("Loi: Vui long nhap so hop le!")

def menu_gf2m8():
    print("\n--- NHAN TRONG TRUONG GF(2^8) ---")
    print("Da thuc toi gian: p(x) = x^8 + x^4 + x^3 + x + 1 (0x11B)")
    try:
        a_str = input("Nhap he so thu nhat a (0-255 hoac hex 0x...): ").strip()
        b_str = input("Nhap he so thu hai b (0-255 hoac hex 0x...): ").strip()
        a = int(a_str, 0)
        b = int(b_str, 0)
        
        if not (0 <= a <= 255 and 0 <= b <= 255):
            print("Loi: Gia tri phai nam trong khoang [0, 255] cua GF(2^8)!")
            return
            
        kq = multiply_gf2m8(a, b)
        print(f"-> Ket qua: {hex(a)} * {hex(b)} = {hex(kq)} (Dec: {kq}, Bin: {bin(kq)})")
    except ValueError:
        print("Loi: Vui long nhap so hop le!")

def main():
    while True:
        print("\n==========================================")
        print("CHUONG TRINH TINH TOAN TRUONG HUU HAN GF")
        print("==========================================")
        print("1. Phep nhan trong GF(2^4)")
        print("2. Phep nhan trong GF(2^8) (Tieu chuan AES)")
        print("3. Thoat chuong trinh")
        choice = input("Chon chuc nang (1-3): ").strip()
        
        if choice == "1":
            menu_gf2m4()
        elif choice == "2":
            menu_gf2m8()
        elif choice == "3":
            print("Tam biet!")
            break
        else:
            print("Lua chon khong hop le, vui long chon lai!")

if __name__ == "__main__":
    main()