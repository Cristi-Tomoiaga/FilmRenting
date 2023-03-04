"""
Test cases for film_service module
"""
import unittest

from domain.exceptions import ValidatorException, RepoException
from domain.validators import FilmValidator
from repositories.film_repository import FilmRepository
from services.film_service import FilmService


class TestCaseFilmService(unittest.TestCase):
    def setUp(self):
        self.__film_valid = FilmValidator()
        self.__film_repo = FilmRepository()
        self.__film_srv = FilmService(self.__film_repo, self.__film_valid)

    def test_add_film(self):
        """
        Test function for add_film
        """
        self.assertEqual(self.__film_repo.size(), 0)
        film = self.__film_srv.add_film(1, "Hacksaw Ridge", "Hacksaw Ridge is a 2016 biographical war film directed by Mel Gibson", "Biographical war")
        self.assertEqual(self.__film_repo.size(), 1)
        films = self.__film_repo.get_all()
        self.assertEqual(films[0], film)

        self.assertRaises(ValidatorException, self.__film_srv.add_film, -1, "2", "3", "")

        self.assertRaises(RepoException, self.__film_srv.add_film, 1, "2", "3", "c")

    def test_get_all_films(self):
        """
        Test function for get_all_films
        """
        str_films = self.__film_srv.get_all_films()
        self.assertEqual(str_films, [])

        film = self.__film_srv.add_film(1, "Hacksaw Ridge", "Hacksaw Ridge is a 2016 biographical war film directed by Mel Gibson", "Biographical war")
        str_films = self.__film_srv.get_all_films()
        self.assertEqual(str_films, [str(film)])

    def test_delete_film(self):
        """
        Test function for delete_film
        """
        self.__film_srv.add_film(1, "Hacksaw Ridge", "Hacksaw Ridge is a 2016 biographical war film directed by Mel Gibson", "Biographical war")
        self.assertEqual(self.__film_repo.size(), 1)

        self.__film_srv.delete_film(1)
        self.assertEqual(self.__film_repo.size(), 0)

        self.assertRaises(RepoException, self.__film_srv.delete_film, 12)

    def test_modify_film(self):
        """
        Test function for modify_film
        """
        self.__film_srv.add_film(1, "Hacksaw Ridge", "Hacksaw Ridge is a 2016 biographical war film directed by Mel Gibson", "Biographical war")

        film = self.__film_srv.modify_film(1, "aa", "bb", "cc")

        films = self.__film_repo.get_all()
        self.assertEqual(films[0], film)

        self.assertRaises(ValidatorException, self.__film_srv.modify_film, -1, "2", "3", "")

        self.assertRaises(RepoException, self.__film_srv.modify_film, 10, "2", "3", "c")

    def test_filter_film_with_prefix(self):
        """
        Test function for filter_film_with_prefix
        """
        film1 = self.__film_srv.add_film(1, "Hacksaw Ridge", "Hacksaw Ridge is a 2016 biographical war film directed by Mel Gibson", "Biographical war")
        film2 = self.__film_srv.add_film(3, "The Shawshank Redemption", "The Shawshank Redemption is a 1994 American drama film written and directed by Frank Darabont", "Drama film ")

        films = self.__film_srv.filter_film_with_prefix("Ha")
        self.assertEqual(films, [str(film1)])

        films = self.__film_srv.filter_film_with_prefix("ffws")
        self.assertEqual(films, [])

        films = self.__film_srv.filter_film_with_prefix("")
        self.assertEqual(films, [str(film1), str(film2)])

    def test_generate_films_random(self):
        """
        Test function for generate_films_random
        """
        x = 10

        self.assertEqual(self.__film_repo.size(), 0)
        self.__film_srv.generate_films_random(x)
        self.assertEqual(self.__film_repo.size(), x)

    def test_find_film_by_title(self):
        """
        Test function for find_film_by_title
        """
        film1 = self.__film_srv.add_film(1, "Hacksaw Ridge", "Hacksaw Ridge is a 2016 biographical war film directed by Mel Gibson", "Biographical war")
        film2 = self.__film_srv.add_film(3, "The Shawshank Redemption", "The Shawshank Redemption is a 1994 American drama film written and directed by Frank Darabont", "Drama film ")

        films = self.__film_srv.find_film_by_title("Home alone")
        self.assertEqual(films, [])

        films = self.__film_srv.find_film_by_title("aw")
        self.assertEqual(films, [film1, film2])

        films = self.__film_srv.find_film_by_title("Hacksaw Ridge")
        self.assertEqual(films, [film1])


if __name__ == '__main__':
    unittest.main()
