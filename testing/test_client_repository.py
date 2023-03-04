"""
Test cases for client_repository module
"""
import unittest

from domain.entities import Client
from domain.exceptions import RepoException
from repositories.client_repository import ClientRepository


class TestCaseClientRepository(unittest.TestCase):
    def setUp(self):
        self.__cl_repo = ClientRepository()
        self.__cl = Client(1, "John Smith", 5211110068801)
        self.__cl1 = Client(1, "Joe Doe", 5211110068801)
        self.__cl2 = Client(2, "Jane Doe", 6211110068801)

    def test_add(self):
        """
        Test function for adding a client to the repository
        """
        self.assertEqual(self.__cl_repo.size(), 0)
        self.__cl_repo.add(self.__cl)
        self.assertEqual(self.__cl_repo.size(), 1)

        with self.assertRaises(RepoException) as cm:
            self.__cl_repo.add(self.__cl)
        self.assertEqual(str(cm.exception), "Id existent")

    def test_get_all(self):
        """
        Test function for get_all
        """
        self.__cl_repo.add(self.__cl1)
        self.__cl_repo.add(self.__cl2)

        self.assertEqual(self.__cl_repo.get_all(), [self.__cl1, self.__cl2])

    def test_find(self):
        """
        Test function for finding a client
        """
        self.__cl_repo.add(self.__cl1)
        self.__cl_repo.add(self.__cl2)

        self.assertEqual(self.__cl_repo.find(1), self.__cl1)

        with self.assertRaises(RepoException) as cm:
            self.__cl_repo.find(3)
        self.assertEqual(str(cm.exception), "Id invalid")

    def test_modify(self):
        """
        Test function for modifying a client
        """
        self.__cl_repo.add(self.__cl1)
        self.__cl_repo.add(self.__cl2)

        cl_new = Client(1, "John Doe", 5211110068801)
        self.__cl_repo.modify(cl_new)

        clients = self.__cl_repo.get_all()
        self.assertEqual(clients[0], cl_new)

        cl_new = Client(3, "John Doe", 5211110068801)
        with self.assertRaises(RepoException) as cm:
            self.__cl_repo.modify(cl_new)
        self.assertEqual(str(cm.exception), "Id invalid")

    def test_delete(self):
        """
        Test function for deleting a client
        """
        self.__cl_repo.add(self.__cl1)
        self.__cl_repo.add(self.__cl2)

        self.assertEqual(self.__cl_repo.size(), 2)
        self.__cl_repo.delete(1)
        self.assertEqual(self.__cl_repo.size(), 1)

        with self.assertRaises(RepoException) as cm:
            self.__cl_repo.delete(10)
        self.assertEqual(str(cm.exception), "Id invalid")

    def test_clear(self):
        """
        Test function for clear
        """
        self.__cl_repo.add(self.__cl1)
        self.__cl_repo.add(self.__cl2)

        self.assertEqual(self.__cl_repo.size(), 2)
        self.__cl_repo.clear()
        self.assertEqual(self.__cl_repo.size(), 0)


if __name__ == '__main__':
    unittest.main()
