"""
Test cases for client_service module
"""
import unittest

from domain.exceptions import ValidatorException, RepoException
from domain.validators import ClientValidator
from repositories.client_repository import ClientRepository
from services.client_service import ClientService


class TestCaseClientService(unittest.TestCase):
    def setUp(self):
        self.__cl_repo = ClientRepository()
        self.__cl_valid = ClientValidator()
        self.__cl_srv = ClientService(self.__cl_repo, self.__cl_valid)

    def test_add_client(self):
        """
        Test function for add_client
        """
        self.assertEqual(self.__cl_repo.size(), 0)
        cl = self.__cl_srv.add_client(1, "John Doe", 5211110068801)
        self.assertEqual(self.__cl_repo.size(), 1)
        clients = self.__cl_repo.get_all()
        self.assertEqual(clients[0], cl)

        self.assertRaises(ValidatorException, self.__cl_srv.add_client, -1, "", 0)

        self.assertRaises(RepoException, self.__cl_srv.add_client, 1, "Jane Doe", 6211110068801)

    def test_get_all_clients(self):  # Black Box Testing
        """
        Test function for get_all_clients
        """
        # clients = self.__cl_srv.get_all_clients()
        # self.assertEqual(clients, [])

        cl = self.__cl_srv.add_client(1, "Joe Doe", 5211110068801)
        clients = self.__cl_srv.get_all_clients()
        self.assertEqual(clients, [str(cl)])

        cl2 = self.__cl_srv.add_client(2, "Jane Doe", 6211110068801)
        clients = self.__cl_srv.get_all_clients()
        self.assertEqual(clients, [str(cl), str(cl2)])

    def test_modify_client(self):
        """
        Test function for modify_client
        """
        self.__cl_srv.add_client(1, "John Doe", 5211110068801)

        cl = self.__cl_srv.modify_client(1, "Joe Doe", 5211110068801)
        clients = self.__cl_repo.get_all()

        self.assertEqual(clients[0], cl)

        self.assertRaises(RepoException, self.__cl_srv.modify_client, 3, "Joe Doe", 5211110068801)

        self.assertRaises(ValidatorException, self.__cl_srv.modify_client, 1, "", 0)

    def test_delete_client(self):
        """
        Test function for delete_client
        """
        self.__cl_srv.add_client(1, "John Doe", 5211110068801)

        self.assertEqual(self.__cl_repo.size(), 1)
        self.__cl_srv.delete_client(1)
        self.assertEqual(self.__cl_repo.size(), 0)

        self.assertRaises(RepoException, self.__cl_srv.delete_client, 10)

    def test_find_client_by_cnp(self):
        """
        Test function for find_client_by_cnp
        """
        cl1 = self.__cl_srv.add_client(1, "John Doe", 5211110068801)
        self.__cl_srv.add_client(2, "Jane Doe", 6211110068801)

        cl = self.__cl_srv.find_client_by_cnp(5211110068801)
        self.assertEqual(cl1, cl)

        with self.assertRaises(RepoException) as cm:
            self.__cl_srv.find_client_by_cnp(5211110068803)
        self.assertEqual(str(cm.exception), "CNP invalid")

    def test_find_client_by_name(self):
        """
        Test function for find_client_by_name
        """
        cl1 = self.__cl_srv.add_client(1, "John Doe", 5211110068801)
        cl2 = self.__cl_srv.add_client(2, "Jane Doe", 6211110068801)

        cls = self.__cl_srv.find_client_by_name("John Doe")
        self.assertEqual(cls, [cl1])

        cls = self.__cl_srv.find_client_by_name("Hugh")
        self.assertEqual(cls, [])

        cls = self.__cl_srv.find_client_by_name("Doe")
        self.assertEqual(cls, [cl1, cl2])

    def test_generate_clients_random(self):
        """
        Test function for generate_clients_random
        """
        x = 10

        self.assertEqual(self.__cl_repo.size(), 0)
        self.__cl_srv.generate_clients_random(x)
        self.assertEqual(self.__cl_repo.size(), x)


if __name__ == '__main__':
    unittest.main()
