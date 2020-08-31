"""
A simple gist to show how to mock private methods.
"""

import unittest
from unittest import mock

class Car:
    def __private1(self):
        return 1

    def __private2(self):
        return 2

    def no_private(self):
        self.__private2()
        return self.__private1()


class CarTest(unittest.TestCase):

    def test_exception_raises(self):
        c = Car()
        with self.assertRaises(AttributeError):
            c.__private()

    def test_car_works(self):
        c = Car()
        self.assertEqual(c.no_private(), 1)

    def test_mock_private(self):
        c = Car()
        with mock.patch.object(c, '_Car__private1', return_value=3) as method1, \
            mock.patch.object(c, '_Car__private2', return_value=4) as method2:
                c.no_private()
                method1.assert_called_once_with()
                method2.assert_called_once_with()


if __name__ == "__main__":
    unittest.main()