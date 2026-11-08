import unittest
from gf2m4 import multiply_gf2m4
from gf2m8 import multiply_gf2m8

class TestGaloisFieldMultiplication(unittest.TestCase):
    def test_gf2m4_identity_and_zero(self):
        # Nhan voi 0 phai bang 0
        self.assertEqual(multiply_gf2m4(0, 11), 0)
        self.assertEqual(multiply_gf2m4(7, 0), 0)
        # Nhan voi 1 phai bang chinh no
        self.assertEqual(multiply_gf2m4(1, 9), 9)
        self.assertEqual(multiply_gf2m4(13, 1), 13)

    def test_gf2m4_calculation(self):
        # 8 * 4 voi p(x) = x^4 + x + 1 (0x13) bang 6 (0x6)
        self.assertEqual(multiply_gf2m4(8, 4), 6)
        # 7 * 3 = 11 (0xb)
        self.assertEqual(multiply_gf2m4(7, 3), 9)

    def test_gf2m8_identity_and_zero(self):
        # Nhan voi 0 phai bang 0
        self.assertEqual(multiply_gf2m8(0x00, 0xAF), 0x00)
        # Nhan voi 1 phai bang chinh no
        self.assertEqual(multiply_gf2m8(0x01, 0x57), 0x57)

    def test_gf2m8_aes_standard_vectors(self):
        # Vector kiem thu chuan tu FIPS 197 (AES Standard)
        # 0x57 * 0x83 = 0xc1
        self.assertEqual(multiply_gf2m8(0x57, 0x83), 0xc1)
        # 0x57 * 0x02 = 0xae
        self.assertEqual(multiply_gf2m8(0x57, 0x02), 0xae)
        # 0x57 * 0x04 = 0x47
        self.assertEqual(multiply_gf2m8(0x57, 0x04), 0x47)

if __name__ == "__main__":
    unittest.main()