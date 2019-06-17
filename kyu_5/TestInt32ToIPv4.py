import unittest

from kyu_5 import Int32ToIPv4


class TestInt32ToIPv4(unittest.TestCase):

    def test_int32_to_IPv4(self):
        self.assertEqual(Int32ToIPv4.int32_to_ip(2154959208), "128.114.17.104")
        self.assertEqual(Int32ToIPv4.int32_to_ip(2149583361), "128.32.10.1")
        self.assertEqual(Int32ToIPv4.int32_to_ip(0), "0.0.0.0")


    def test_to_bytes(self):
        self.assertEqual(Int32ToIPv4.bits_to_bytes("10000000001000000000101000000001"), "128.32.10.1")
        self.assertEqual(Int32ToIPv4.bits_to_bytes("00000000000000000000000000000000"), "0.0.0.0")

    def test_to_binary(self):
        self.assertEqual(Int32ToIPv4.int32_to_bits(0), "00000000000000000000000000000000")
        self.assertEqual(Int32ToIPv4.int32_to_bits(2149583361), "10000000001000000000101000000001")


if __name__ == '__main__':
    unittest.main()
