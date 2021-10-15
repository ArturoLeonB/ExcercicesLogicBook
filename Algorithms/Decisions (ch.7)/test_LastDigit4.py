import unittest
import LastDigit4

class MyTestCase(unittest.TestCase):
    def test_LastDigit4(self):
        self.assertEqual(LastDigit4.Ult_Dig_4(64), 4)  # add assertion here


if __name__ == '__main__':
    unittest.main()
