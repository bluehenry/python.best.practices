import unittest
from utilities.url_utilities import load_urls_from_file

#
# def test_load_file():
#     test_urls = load_urls_from_file("input.txt")
#     assert (len(test_urls) > 1)

class UrlUtilitiesTest(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_load_file(self):
        test_urls = load_urls_from_file("../../input.txt")
        assert (len(test_urls) > 1)
