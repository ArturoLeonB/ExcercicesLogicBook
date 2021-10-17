import unittest
from Algorithms.src.Decisions import Decisions

class test_Decisions(unittest.TestCase):
    def test_num_ends_with_4(self):
        self.assertEqual(Decisions.num_ends_with_4(self, 34), True)  # add assertion here


if __name__ == '__main__':
    unittest.main()
