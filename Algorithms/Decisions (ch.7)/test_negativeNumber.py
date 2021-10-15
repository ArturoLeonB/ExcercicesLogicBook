import unittest

def is_this_number_negative(num):
    if num < 0:
        print ("negative")
    else:
        print ("Is not negative")

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertTrue(num)  # add assertion here


if __name__ == '__main__':
    unittest.main()
