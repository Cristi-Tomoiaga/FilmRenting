"""
Test cases for transaction_service module
"""
import os.path
import unittest

from domain.datatransfer import ClientDTO, FilmDTO
from domain.entities import Film, Client
from domain.exceptions import RepoException, ValidatorException
from domain.validators import TransactionValidator, FilmValidator, ClientValidator
from repositories.client_file_repository import ClientFileRepository
from repositories.client_repository import ClientRepository
from repositories.film_file_repository import FilmFileRepository
from repositories.film_repository import FilmRepository
from repositories.transaction_file_repository import TransactionFileRepository
from repositories.transaction_repository import TransactionRepository
from services.client_service import ClientService
from services.film_service import FilmService
from services.transaction_service import TransactionService


class TestCaseTransactionService(unittest.TestCase):
    def setUp(self):
        if os.path.exists("test_films.txt"):
            os.remove("test_films.txt")
        if os.path.exists("test_clients.txt"):
            os.remove("test_clients.txt")
        if os.path.exists("test_transactions.txt"):
            os.remove("test_transactions.txt")

        self.__film_repo = FilmRepository()
        # self.__film_repo = FilmFileRepository("test_films.txt")
        self.__film_valid = FilmValidator()
        self.__film_srv = FilmService(self.__film_repo, self.__film_valid)

        self.__client_repo = ClientRepository()
        # self.__client_repo = ClientFileRepository("test_clients.txt")
        self.__client_valid = ClientValidator()
        self.__client_srv = ClientService(self.__client_repo, self.__client_valid)

        self.__tr_repo = TransactionRepository()
        # self.__tr_repo = TransactionFileRepository("test_transactions.txt", self.__film_repo, self.__client_repo)
        self.__tr_valid = TransactionValidator()
        self.__tr_srv = TransactionService(self.__tr_repo, self.__tr_valid, self.__film_repo, self.__client_repo)

    def tearDown(self):
        if os.path.exists("test_films.txt"):
            os.remove("test_films.txt")
        if os.path.exists("test_clients.txt"):
            os.remove("test_clients.txt")
        if os.path.exists("test_transactions.txt"):
            os.remove("test_transactions.txt")

    def test_rent_film_to_client(self):
        """
        Test function for rent_film_to_client
        """
        film = Film(1, "film1", "desc1", "gen1")
        film2 = Film(2, "film2", "desc2", "gen2")
        self.__film_repo.add(film)
        self.__film_repo.add(film2)

        client = Client(1, "nume1", 5211110068801)
        client2 = Client(2, "nume2", 5211110068823)
        self.__client_repo.add(client)
        self.__client_repo.add(client2)

        self.assertEqual(self.__tr_repo.size(), 0)
        self.__tr_srv.rent_film_to_client(1, film.get_id(), client.get_id())
        self.assertEqual(self.__tr_repo.size(), 1)

        self.assertRaises(RepoException, self.__tr_srv.rent_film_to_client, 1, film.get_id(), client.get_id())

        with self.assertRaises(RepoException) as cm:
            self.__tr_srv.rent_film_to_client(2, film.get_id(), client2.get_id())
        self.assertEqual(str(cm.exception), "Filmul este deja inchiriat")

        self.assertRaises(RepoException, self.__tr_srv.rent_film_to_client, 2, 4, 6)

        self.assertRaises(ValidatorException, self.__tr_srv.rent_film_to_client, -1, film2.get_id(), client2.get_id())

    def test_return_film_from_client(self):
        """
        Test function for return_film_from_client
        """
        film = Film(1, "film1", "desc1", "gen1")
        film2 = Film(2, "film2", "desc2", "gen2")
        self.__film_repo.add(film)
        self.__film_repo.add(film2)

        client = Client(1, "nume1", 5211110068801)
        client2 = Client(2, "nume2", 5211110068823)
        self.__client_repo.add(client)
        self.__client_repo.add(client2)

        self.__tr_srv.rent_film_to_client(1, film.get_id(), client.get_id())
        self.__tr_srv.return_film_from_client(film.get_id(), client.get_id())

        self.assertRaises(RepoException, self.__tr_srv.return_film_from_client, film.get_id(), client.get_id())

        self.assertRaises(RepoException, self.__tr_srv.return_film_from_client, film2.get_id(), client2.get_id())

        self.assertRaises(RepoException, self.__tr_srv.return_film_from_client, -3, 6)

    def test_generate_transactions_random(self):
        """
        Test function for generate_transactions_random
        """
        x = 10
        self.__film_srv.generate_films_random(x)
        self.__client_srv.generate_clients_random(x)

        self.assertEqual(self.__tr_repo.size(), 0)
        self.__tr_srv.generate_transactions_random(x)
        self.assertEqual(self.__tr_repo.size(), x)

        self.__tr_repo.clear()
        self.assertEqual(self.__tr_repo.size(), 0)
        self.__tr_srv.generate_transactions_random(x, tweak=True)
        self.assertEqual(self.__tr_repo.size(), x)

    def test_report_clients_by_name(self):
        """
        Test function for report_clients_by_name
        """
        self.assertEqual(self.__tr_srv.report_clients_by_name(), [])

        film = Film(1, "film1", "desc1", "gen1")
        film2 = Film(2, "film2", "desc2", "gen2")
        self.__film_repo.add(film)
        self.__film_repo.add(film2)

        client = Client(1, "nume1", 5211110068801)
        client2 = Client(2, "nume2", 5211110068823)
        self.__client_repo.add(client)
        self.__client_repo.add(client2)

        self.__tr_srv.rent_film_to_client(1, film.get_id(), client.get_id())
        self.__tr_srv.rent_film_to_client(2, film2.get_id(), client.get_id())
        self.__tr_srv.return_film_from_client(film2.get_id(), client.get_id())
        self.__tr_srv.rent_film_to_client(1, film2.get_id(), client2.get_id())

        cldto1 = ClientDTO(client.get_id(), client.get_name())
        cldto1.add_film(film)
        cldto1.add_film(film2)

        cldto2 = ClientDTO(client2.get_id(), client2.get_name())
        cldto2.add_film(film2)

        self.assertEqual(self.__tr_srv.report_clients_by_name(), [str(cldto1), str(cldto2)])

        self.__tr_repo.clear()
        self.__client_repo.clear()
        self.__film_repo.clear()
        self.assertEqual(self.__tr_srv.report_clients_by_name(), [])

    def test_report_clients_by_number(self):
        """
        Test function for report_clients_by_number
        """
        self.assertEqual(self.__tr_srv.report_clients_by_number(), [])

        film = Film(1, "film1", "desc1", "gen1")
        film2 = Film(2, "film2", "desc2", "gen2")
        self.__film_repo.add(film)
        self.__film_repo.add(film2)

        client = Client(1, "nume1", 5211110068801)
        client2 = Client(2, "nume2", 5211110068823)
        self.__client_repo.add(client)
        self.__client_repo.add(client2)

        self.__tr_srv.rent_film_to_client(1, film.get_id(), client.get_id())
        self.__tr_srv.rent_film_to_client(2, film2.get_id(), client.get_id())
        self.__tr_srv.return_film_from_client(film2.get_id(), client.get_id())
        self.__tr_srv.rent_film_to_client(1, film2.get_id(), client2.get_id())

        cldto1 = ClientDTO(client.get_id(), client.get_name())
        cldto1.add_film(film)
        cldto1.add_film(film2)

        cldto2 = ClientDTO(client2.get_id(), client2.get_name())
        cldto2.add_film(film2)

        self.assertEqual(self.__tr_srv.report_clients_by_number(), [str(cldto1), str(cldto2)])

    def test_report_films(self):
        """
        Test function for report_films
        """
        self.assertEqual(self.__tr_srv.report_films(), [])

        film = Film(1, "film1", "desc1", "gen1")
        film2 = Film(2, "film2", "desc2", "gen2")
        self.__film_repo.add(film)
        self.__film_repo.add(film2)

        client = Client(1, "nume1", 5211110068801)
        client2 = Client(2, "nume2", 5211110068823)
        self.__client_repo.add(client)
        self.__client_repo.add(client2)

        self.__tr_srv.rent_film_to_client(1, film.get_id(), client.get_id())
        self.__tr_srv.rent_film_to_client(2, film2.get_id(), client.get_id())
        self.__tr_srv.return_film_from_client(film2.get_id(), client.get_id())
        self.__tr_srv.rent_film_to_client(1, film2.get_id(), client2.get_id())

        flmdto1 = FilmDTO(film.get_id(), film.get_title())
        flmdto1.inc_num_rent()

        flmdto2 = FilmDTO(film2.get_id(), film2.get_title())
        flmdto2.inc_num_rent()
        flmdto2.inc_num_rent()

        assert self.__tr_srv.report_films() == [str(flmdto2), str(flmdto1)]

    def test_report_first_clients(self):
        """
        Test function for report_first_clients
        """
        self.assertEqual(self.__tr_srv.report_first_clients(), [])

        film = Film(1, "film1", "desc1", "gen1")
        film2 = Film(2, "film2", "desc2", "gen2")
        self.__film_repo.add(film)
        self.__film_repo.add(film2)

        client = Client(1, "nume1", 5211110068801)
        client2 = Client(2, "nume2", 5211110068823)
        client3 = Client(3, "nume3", 6211110068823)
        self.__client_repo.add(client)
        self.__client_repo.add(client2)
        self.__client_repo.add(client3)

        self.__tr_srv.rent_film_to_client(1, film.get_id(), client.get_id())
        self.__tr_srv.rent_film_to_client(2, film2.get_id(), client.get_id())
        self.__tr_srv.return_film_from_client(film2.get_id(), client.get_id())
        self.__tr_srv.rent_film_to_client(1, film2.get_id(), client2.get_id())

        cldto1 = ClientDTO(client.get_id(), client.get_name())
        cldto1.add_film(film)
        cldto1.add_film(film2)

        self.assertEqual(self.__tr_srv.report_first_clients(), [str(cldto1)])

        client4 = Client(4, "nume4", 6211130068823)
        self.__client_repo.add(client4)

        cldto2 = ClientDTO(client2.get_id(), client2.get_name())
        cldto2.add_film(film2)

        self.assertEqual(self.__tr_srv.report_first_clients(), [str(cldto1), str(cldto2)])

    def test_report_last_films(self):
        """
        Test function for report_last_films
        """
        self.assertEqual(self.__tr_srv.report_last_films(""), [])

        film = Film(1, "film1", "desc1", "gen1")
        film2 = Film(2, "film2", "desc2", "gen2")
        film3 = Film(3, "film3", "desc3", "gen3")
        film4 = Film(4, "film4", "desc4", "gen4")
        self.__film_repo.add(film)
        self.__film_repo.add(film2)
        self.__film_repo.add(film3)
        self.__film_repo.add(film4)

        client = Client(1, "nume1", 5211110068801)
        client2 = Client(2, "nume2", 5211110068823)
        self.__client_repo.add(client)
        self.__client_repo.add(client2)

        self.__tr_srv.rent_film_to_client(1, film.get_id(), client.get_id())
        self.__tr_srv.rent_film_to_client(2, film2.get_id(), client.get_id())
        self.__tr_srv.return_film_from_client(film2.get_id(), client.get_id())
        self.__tr_srv.rent_film_to_client(1, film2.get_id(), client2.get_id())

        flmdto1 = FilmDTO(film.get_id(), film.get_title())
        flmdto1.inc_num_rent()

        flmdto2 = FilmDTO(film2.get_id(), film2.get_title())
        flmdto2.inc_num_rent()
        flmdto2.inc_num_rent()

        flmdto3 = FilmDTO(film3.get_id(), film3.get_title())
        flmdto4 = FilmDTO(film4.get_id(), film4.get_title())

        self.assertEqual(self.__tr_srv.report_last_films("fi"), [str(flmdto3), str(flmdto4)])


if __name__ == '__main__':
    unittest.main()
