import unittest

from kyu_6 import JumpingSpider


class TestJumperSpiderTest(unittest.TestCase):

    def test_triangle(self):
        self.assertAlmostEqual(JumpingSpider.spider_to_fly("H3", "E2"), 4.635221825785533)

    def test_point(self):
        self.assertEqual(JumpingSpider.spider_to_fly("C2", "C2"), 0)

    def test_line(self):
        self.assertEqual(JumpingSpider.spider_to_fly("G4", "A0"), 4)
        self.assertEqual(JumpingSpider.spider_to_fly("G4", "C4"), 8)


if __name__ == '__main__':
    unittest.main()
