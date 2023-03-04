"""
Test cases for datatransfer module
"""
import unittest

from domain.entities import Film, Client, Transaction
from domain.exceptions import ValidatorException
from domain.validators import FilmValidator, ClientValidator, TransactionValidator


class TestCaseValidators(unittest.TestCase):
    def setUp(self):
        self.__film_validator = FilmValidator()
        self.__client_valid = ClientValidator()
        self.__tr_valid = TransactionValidator()

    def test_validate_film(self):
        """
        Test function for film validation
        """
        film = Film(1, "Hacksaw Ridge", "Hacksaw Ridge is a 2016 biographical war film directed by Mel Gibson",
                    "Biographical war")
        self.__film_validator.validate(film)

        film_all = Film(-2, "", "", "")
        with self.assertRaises(ValidatorException) as cm:
            self.__film_validator.validate(film_all)
        self.assertEqual(str(cm.exception), "Id invalid\nTitlu invalid\nDescriere invalida\nGen invalid\n")

        film_all_but_id = Film(1, "", "", "")
        with self.assertRaises(ValidatorException) as cm:
            self.__film_validator.validate(film_all_but_id)
        self.assertEqual(str(cm.exception), "Titlu invalid\nDescriere invalida\nGen invalid\n")

        film_but_description_genre = Film(1, "Titlu", "", "")
        with self.assertRaises(ValidatorException) as cm:
            self.__film_validator.validate(film_but_description_genre)
        self.assertEqual(str(cm.exception), "Descriere invalida\nGen invalid\n")

    def test_validate_client(self):
        """
        Test function for client validation
        """
        cl = Client(1, "Joe Doe", 5211110068801)
        self.__client_valid.validate(cl)

        cl = Client(-1, "", 0)
        with self.assertRaises(ValidatorException) as cm:
            self.__client_valid.validate(cl)
        self.assertEqual(str(cm.exception), "Id invalid\nNume invalid\nCNP invalid\n")

        cl = Client(1, "", 0)
        with self.assertRaises(ValidatorException) as cm:
            self.__client_valid.validate(cl)
        self.assertEqual(str(cm.exception), "Nume invalid\nCNP invalid\n")

        cl = Client(-1, "", 5211110068801)
        with self.assertRaises(ValidatorException) as cm:
            self.__client_valid.validate(cl)
        self.assertEqual(str(cm.exception), "Id invalid\nNume invalid\n")

    def test_validate_transaction(self):
        """
        Test function for transaction validation
        """
        film = Film(1, "film1", "desc1", "gen1")
        cl = Client(1, "nume", 5211110068801)

        tr = Transaction(1, film, cl)
        self.__tr_valid.validate(tr)

        tr = Transaction(-1, film, cl)
        with self.assertRaises(ValidatorException) as cm:
            self.__tr_valid.validate(tr)
        self.assertEqual(str(cm.exception), "Id invalid\n")


if __name__ == '__main__':
    unittest.main()
