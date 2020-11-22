import unittest


class StringTest(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_lookup_by_name(self):
        print('hello'.capitalize())
        print('hello'.replace('e', 'a'))
        print('hello'.isalpha())
        print('hello'.isdigit())
        print('10'.isdecimal())  # True

    def test_string_interpolation(self):
        name = "Tom"
        str = f'{{name}}'
        print(str)


key = ''
if key != '':
    print('key has something')
else:
    print('key is empty string')

