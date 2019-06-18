import unittest


from kyu_6 import FindMissingLetter


class TestFindMissingLetter(unittest.TestCase):

    def test_find_missing_letter(self):
        self.assertEqual(FindMissingLetter.find_missing_letter(['a', 'b', 'c', 'd', 'f']), 'e')
        self.assertEqual(FindMissingLetter.find_missing_letter(['O', 'Q', 'R', 'S']), 'P')


if __name__ == '__main__':
    unittest.main()
