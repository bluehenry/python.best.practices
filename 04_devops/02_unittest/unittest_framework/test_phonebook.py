import unittest

from phonebook import PhoneBook


class PhoneBookTest(unittest.TestCase):

    def setUp(self) -> None:
        self.phonebook = PhoneBook()

    def tearDown(self) -> None:
        pass

    # Test Case Name
    def test_lookup_by_name(self):
        # Arrange
        self.phonebook.add('Bob', '12345')

        # Act
        number = self.phonebook.lookup('Bob')

        # Assert
        self.assertEqual('12345', number)

    def test_is_consistent(self):
        self.assertTrue(self.phonebook.is_consistent())

    def test_is_consistent_with_diffirent_entries(self):
        self.phonebook.add('Bob', '12345')
        self.phonebook.add('Anna', '012345')
        self.assertTrue(self.phonebook.is_consistent())

    def test_inconsistent_with_duplicate_entries(self):
        self.phonebook.add('Bob', '12345')
        self.phonebook.add('Anna', '12345')
        self.assertFalse(self.phonebook.is_consistent())

    # WIP: Work In Progress
    # @unittest.skip('WIP')
    def test_inconsistent_with_duplicate_prefix(self):
        self.phonebook.add('Bob', '12345')
        self.phonebook.add('Anna', '123')
        self.assertFalse(self.phonebook.is_consistent())

    def test_missing_name(self):
        with self.assertRaises(KeyError):
            self.phonebook.lookup('missing')



