"""
Test cases for entities module
"""
import datetime
import unittest

from domain.entities import Film, Client, Transaction


class TestCaseFilm(unittest.TestCase):
    def setUp(self):
        self.__film = Film(1, "Hacksaw Ridge", "Hacksaw Ridge is a 2016 biographical war film directed by Mel Gibson", "Biographical war")
        self.__film2 = Film(1, "", "", "")
        self.__film3 = Film(3, "The Shawshank Redemption", "The Shawshank Redemption is a 1994 American drama film written and directed by Frank Darabont", "Drama film")

    def test_create(self):
        """
        Test function for the creation of a film object
        """
        self.assertEqual(self.__film.get_id(), 1)
        self.assertEqual(self.__film.get_title(), "Hacksaw Ridge")
        self.assertEqual(self.__film.get_description(), "Hacksaw Ridge is a 2016 biographical war film directed by Mel Gibson")
        self.assertEqual(self.__film.get_genre(), "Biographical war")
        self.__film.set_title("Hacksaw")
        self.__film.set_genre("Biographical")
        self.__film.set_description("Hacksaw Ridge")
        self.assertEqual(self.__film.get_title(), "Hacksaw")
        self.assertEqual(self.__film.get_description(), "Hacksaw Ridge")
        self.assertEqual(self.__film.get_genre(), "Biographical")

    def test_equal(self):
        """
        Test function for the == operator
        """
        self.assertEqual(self.__film, self.__film2)
        self.assertNotEqual(self.__film, self.__film3)

    def test_string(self):
        """
        Test for the string representation of a film
        """
        self.assertEqual(str(self.__film), "1. Hacksaw Ridge, Hacksaw Ridge is a 2016 biographical war film directed by Mel Gibson, Biographical war")


class TestCaseClient(unittest.TestCase):
    def setUp(self):
        self.__cl1 = Client(1, "John Doe Sr", 5211110068801)
        self.__cl2 = Client(1, "John Doe", 5211110068801)
        self.__cl3 = Client(2, "Jane Doe", 6211110068801)
        self.__cl = Client(12, "Joe Doe", 5211110068801)

    def test_create(self):
        """
        Test function for the creation of a client object
        """
        self.assertEqual(self.__cl.get_id(), 12)
        self.assertEqual(self.__cl.get_name(), "Joe Doe")
        self.assertEqual(self.__cl.get_cnp(), 5211110068801)
        self.__cl.set_cnp(6211110068801)
        self.__cl.set_name("Jane Doe")
        self.assertEqual(self.__cl.get_name(), "Jane Doe")
        self.assertEqual(self.__cl.get_cnp(), 6211110068801)

    def test_equal(self):
        """
        Test function for the == operator
        """
        self.assertEqual(self.__cl1, self.__cl2)
        self.assertNotEqual(self.__cl1, self.__cl3)

    def test_string(self):
        """
        Test function for the string representation of a client
        """
        self.assertEqual(str(self.__cl), "Id: 12, Nume: Joe Doe, CNP: 5211110068801")


class TestCaseTransaction(unittest.TestCase):
    def setUp(self):
        self.__film = Film(1, "film1", "desc1", "gen1")
        self.__cl = Client(1, "nume", 5211110068801)
        self.__tr = Transaction(1, self.__film, self.__cl)

        film = Film(1, "film1", "desc1", "gen1")
        cl = Client(1, "nume", 5211110068801)
        self.__tr2 = Transaction(2, film, cl)

        film2 = Film(2, "film2", "desc2", "gen2")
        cl = Client(1, "nume", 5211110068801)
        self.__tr3 = Transaction(1, film2, cl)

        film = Film(1, "film1", "desc1", "gen1")
        cl = Client(1, "nume", 5211110068801)
        self.__tr4 = Transaction(1, film, cl)

    def test_create(self):
        """
        Test function for the creation of a transaction
        """
        self.assertEqual(self.__tr.get_id(), 1)
        self.assertEqual(self.__tr.get_film(), self.__film)
        self.assertEqual(self.__tr.get_client(), self.__cl)

        dt = datetime.datetime.now()
        self.__tr.set_date(dt)
        self.assertEqual(self.__tr.get_date(), dt)

        self.__tr.set_returned(True)
        self.assertTrue(self.__tr.is_returned())

        self.__tr.set_returned(False)
        self.assertFalse(self.__tr.is_returned())

        self.assertFalse(self.__tr.is_returned())
        self.__tr.return_transaction()
        self.assertTrue(self.__tr.is_returned())

    def test_equal(self):
        """
        Test function for the == operator
        """
        self.assertEqual(self.__tr, self.__tr)
        self.assertEqual(self.__tr, self.__tr4)
        self.assertNotEqual(self.__tr, self.__tr2)
        self.assertNotEqual(self.__tr, self.__tr3)

    def test_string(self):
        """
        Test function for string representation of a transaction
        """
        self.assertEqual(str(self.__tr), f"Id_tranzactie: 1, Id_film: 1, Id_client: 1, Data: {self.__tr.get_date().strftime('%d.%m.%Y')}, Ora: {self.__tr.get_date().strftime('%H:%M')}, Returnat: False")


if __name__ == '__main__':
    unittest.main()
