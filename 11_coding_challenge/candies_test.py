import unittest
from candies import candies

class CandiesTest (unittest.TestCase):

    def test_case1(self):
        self.assertEqual(candies(3, [1,2,2]), 4)

    def test_case2(self):
        self.assertEqual(candies(10, [2,4,2,6,1,7,8,9,2,1]), 19)

    def test_case3(self):
        self.assertEqual(candies(8, [2,4,3,5,2,6,4,5]), 12)

if __name__ == '__main__':
        unittest.main()
