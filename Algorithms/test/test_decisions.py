import unittest
from Algorithms.src.Decisions import Decisions

class test_Decisions(unittest.TestCase):
    def setUp(self):
        self.decisions = Decisions()

    def test_num_ends_with_4(self):
        self.assertEqual(self.decisions.num_ends_with_4(34), True) # add assertion here
        self.assertEqual(self.decisions.num_ends_with_4(35), False)
        self.assertEqual(self.decisions.num_ends_with_4(3452), False)
        self.assertEqual(self.decisions.num_ends_with_4(14), True)
        self.assertFalse(self.decisions.num_ends_with_4(99))
        self.assertTrue(self.decisions.num_ends_with_4(-24))

    def test_num_with_three_digits(self):
        self.assertEqual(self.decisions.num_with_three_digits(99 + 1), True)
        self.assertEqual(self.decisions.num_with_three_digits(123), True)
        self.assertTrue(self.decisions.num_with_three_digits(-555))
        self.assertFalse(self.decisions.num_with_three_digits(9999))
        self.assertFalse(self.decisions.num_with_three_digits(000))
        self.assertEqual(self.decisions.num_with_three_digits(10), False)

    def test_is_this_number_negative(self):
        self.assertEqual(self.decisions.is_this_number_negative(24), False)
        self.assertTrue(self.decisions.is_this_number_negative(-1))
        self.assertFalse(self.decisions.is_this_number_negative(45))
        self.assertTrue(self.decisions.is_this_number_negative(2 - 3))
        self.assertTrue(self.decisions.is_this_number_negative(-200))
        self.assertFalse(self.decisions.is_this_number_negative(12))

    def test_sum_digits_number(self):
        self.assertEqual(self.decisions.sum_digits_number(70), 7)
        self.assertEqual(self.decisions.sum_digits_number(34), 7)
        self.assertEqual(self.decisions.sum_digits_number(23), 5)
        self.assertNotEqual(self.decisions.sum_digits_number(45), 10)
        self.assertNotEqual(self.decisions.sum_digits_number(13), 5)

    def test_two_digits_pair(self):
        self.assertTrue(self.decisions.two_digits_pair(88), True)
        self.assertTrue(self.decisions.two_digits_pair(22))
        self.assertFalse(self.decisions.two_digits_pair(23))
        self.assertFalse(self.decisions.two_digits_pair(11))
        self.assertTrue(self.decisions.two_digits_pair(82))

if __name__ == '__main__':
    unittest.main()
