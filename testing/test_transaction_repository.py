"""
Test cases for transaction_repository module
"""
import unittest

from domain.entities import Film, Client, Transaction
from domain.exceptions import RepoException
from repositories.transaction_repository import TransactionRepository


class TestCaseTransactionRepository(unittest.TestCase):
    def setUp(self):
        self.__tr_repo = TransactionRepository()
        self.__film = Film(1, "film1", "desc1", "gen1")
        self.__cl = Client(1, "nume", 5211110068801)
        self.__tr = Transaction(1, self.__film, self.__cl)

    def test_add(self):
        """
        Test function for adding a transaction to the repository
        """
        self.assertEqual(self.__tr_repo.size(), 0)

        self.__tr_repo.add(self.__tr)

        self.assertEqual(self.__tr_repo.size(), 1)

        with self.assertRaises(RepoException) as cm:
            self.__tr_repo.add(self.__tr)
        self.assertEqual(str(cm.exception), "Id existent pentru inchiriere")

    def test_return_transaction(self):
        """
        Test function for returning transactions in the repository
        """
        self.__tr_repo.add(self.__tr)
        self.assertFalse(self.__tr.is_returned())

        self.__tr_repo.return_transaction(self.__tr.get_film(), self.__tr.get_client())
        self.assertRaises(RepoException, self.__tr_repo.find_by_film_client, self.__tr.get_film(), self.__tr.get_client())

        film2 = Film(2, "film2", "desc2", "gen2")
        cl2 = Client(2, "nume2", 6211110068801)
        with self.assertRaises(RepoException) as cm:
            self.__tr_repo.return_transaction(film2, cl2)
        self.assertEqual(str(cm.exception), "Inchiriere inexistenta")

    def test_find_by_film_client(self):
        """
        Test function for find_by_film_client
        """
        self.__tr.return_transaction()
        self.__tr_repo.add(self.__tr)
        tr2 = Transaction(2, self.__film, self.__cl)
        self.__tr_repo.add(tr2)

        self.assertEqual(self.__tr_repo.find_by_film_client(self.__film, self.__cl), tr2)

        film2 = Film(2, "film2", "desc2", "gen2")
        with self.assertRaises(RepoException) as cm:
            self.__tr_repo.find_by_film_client(film2, self.__cl)
        self.assertEqual(str(cm.exception), "Inchiriere inexistenta")

    def test_is_film_rented(self):
        """
        Test function for is_film_rented
        """
        self.__tr.return_transaction()
        self.__tr_repo.add(self.__tr)
        tr2 = Transaction(2, self.__film, self.__cl)
        self.__tr_repo.add(tr2)

        self.assertTrue(self.__tr_repo.is_film_rented(self.__film))

        film2 = Film(2, "film2", "desc2", "gen2")
        self.assertFalse(self.__tr_repo.is_film_rented(film2))

        self.__tr_repo.return_transaction(tr2.get_film(), tr2.get_client())
        self.assertFalse(self.__tr_repo.is_film_rented(self.__film))

    def test_clear(self):
        """
        Test function for clear
        """
        self.__tr.return_transaction()
        self.__tr_repo.add(self.__tr)
        tr2 = Transaction(2, self.__film, self.__cl)
        self.__tr_repo.add(tr2)

        self.assertEqual(self.__tr_repo.size(), 2)
        self.__tr_repo.clear()
        self.assertEqual(self.__tr_repo.size(), 0)

    def test_get_all_for_client(self):
        """
        Test function for get_all_for_client
        """
        cl2 = Client(2, "nume2", 6211110068801)
        self.assertEqual(self.__tr_repo.get_all_for_client(self.__cl), [])

        self.__tr_repo.add(self.__tr)

        self.assertEqual(self.__tr_repo.get_all_for_client(self.__cl),  [self.__tr])
        self.assertEqual(self.__tr_repo.get_all_for_client(cl2), [])

    def test_get_all_for_film(self):
        """
        Test function for get_all_for_film
        """
        film2 = Film(2, "film2", "desc2", "gen2")
        self.assertEqual(self.__tr_repo.get_all_for_film(self.__film), [])

        self.__tr_repo.add(self.__tr)

        self.assertEqual(self.__tr_repo.get_all_for_film(self.__film), [self.__tr])
        self.assertEqual(self.__tr_repo.get_all_for_film(film2), [])


if __name__ == '__main__':
    unittest.main()
