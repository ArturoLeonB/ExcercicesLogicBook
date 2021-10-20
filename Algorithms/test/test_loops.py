import unittest
from Algorithms.src.Loops import Loops

class test_Loops(unittest.TestCase):

    def setUp(self):
        self.loops = Loops()


    def test_pair_list(self):
        self.assertEqual(self.loops.pair_list())

    def test_all_submultiples(self):
        self.assertEqual(self.loops.all_submultiples())

    def test_all_int_between(self):
        self.assertEqual(self.loops.test_all_int_between())

    def test_all_num_ends_4(self):
        self.assertEqual(self.loops.all_numbers_ends_4())

if __name__ == '__main__':
    unittest.main()
