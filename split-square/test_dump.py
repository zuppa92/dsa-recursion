import unittest
from dump import dump

class TestDumpFunction(unittest.TestCase):
    def test_simple_squares(self):
        self.assertEqual(dump(0), "0")
        self.assertEqual(dump(1), "1")
    
    def test_split_squares(self):
        self.assertEqual(dump([0, 1, 0, 1]), "0 1 0 1")
        self.assertEqual(dump([0, 0, 0, [1, 1, 1, 1]]), "0 0 0 1 1 1 1")
        self.assertEqual(dump([0, 0, 0, [1, 1, 1, [0, 0, 0, [1, 1, 1, 1]]]]), "0 0 0 1 1 1 0 0 0 1 1 1 1")

if __name__ == "__main__":
    unittest.main()
