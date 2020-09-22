import unittest

from phone_book import PhoneBook


class PhoneBookTest(unittest.TestCase):

    def setUp(self) -> None:
        self.phone_book = PhoneBook()

    def tearDown(self) -> None:
        pass

    # Test Case Name
    def test_lookup_by_name(self):
        # Arrange
        self.phone_book.add('Bob', '12345')

        # Act
        number = self.phone_book.lookup('Bob')

        # Assert
        self.assertEqual('12345', number)

    def test_is_consistent(self):
        self.assertTrue(self.phone_book.is_consistent())

    def test_is_consistent_with_diffirent_entries(self):
        self.phone_book.add('Bob', '12345')
        self.phone_book.add('Anna', '012345')
        self.assertTrue(self.phone_book.is_consistent())

    def test_inconsistent_with_duplicate_entries(self):
        self.phone_book.add('Bob', '12345')
        self.phone_book.add('Anna', '12345')
        self.assertFalse(self.phone_book.is_consistent())

    # WIP: Work In Progress
    # @unittest.skip('WIP')
    def test_inconsistent_with_duplicate_prefix(self):
        self.phone_book.add('Bob', '12345')
        self.phone_book.add('Anna', '123')
        self.assertFalse(self.phone_book.is_consistent())

    def test_missing_name(self):
        with self.assertRaises(KeyError):
            self.phone_book.lookup('missing')



