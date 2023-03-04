"""
Test cases for film_file_repository module
"""
import os
import unittest

from domain.entities import Film
from domain.exceptions import RepoException
from repositories.film_file_repository import FilmFileRepository


class TestCaseFilmFileRepository(unittest.TestCase):
    def setUp(self):
        if os.path.exists("test_films.txt"):
            os.remove("test_films.txt")
        self.__film_repo = FilmFileRepository("test_films.txt")
        self.__film = Film(1, "Hacksaw Ridge", "Hacksaw Ridge is a 2016 biographical war film directed by Mel Gibson", "Biographical war")
        self.__film_ = Film(3, "Hacksaw Ridge", "Hacksaw Ridge is a 2016 biographical war film directed by Mel Gibson", "Biographical war")
        self.__film1 = Film(1, "Hacksaw Ridge", "Hacksaw Ridge is a 2016 biographical war film directed by Mel Gibson", "Biographical war")
        self.__film2 = Film(3, "The Shawshank Redemption", "The Shawshank Redemption is a 1994 American drama film written and directed by Frank Darabont", "Drama film ")

    def tearDown(self):
        if os.path.exists("test_films.txt"):
            os.remove("test_films.txt")

    def test_add(self):
        """
        Test function for adding a film to the repository
        """
        self.assertEqual(self.__film_repo.size(), 0)
        self.__film_repo.add(self.__film)
        self.assertEqual(self.__film_repo.size(), 1)

        film_all = Film(1, "", "", "")
        with self.assertRaises(RepoException) as cm:
            self.__film_repo.add(film_all)
        self.assertEqual(str(cm.exception), "Id existent")

    def test_get_all(self):
        """
        Test function for get_all
        """
        self.assertEqual(self.__film_repo.get_all(), [])

        self.__film_repo.add(self.__film1)
        self.__film_repo.add(self.__film2)

        self.assertEqual(self.__film_repo.get_all(), [self.__film1, self.__film2])

    def test_delete(self):
        """
        Test function for deleting a film from the repository
        """
        self.__film_repo.add(self.__film)

        self.assertEqual(self.__film_repo.size(), 1)
        self.__film_repo.delete(1)
        self.assertEqual(self.__film_repo.size(), 0)

        with self.assertRaises(RepoException) as cm:
            self.__film_repo.delete(20)
        self.assertEqual(str(cm.exception), "Id invalid")

    def test_find(self):
        """
        Test function for finding a film
        """
        self.__film_repo.add(self.__film)

        self.assertEqual(self.__film_repo.find(1), self.__film)

        with self.assertRaises(RepoException) as cm:
            self.__film_repo.find(2)
        self.assertEqual(str(cm.exception), "Id invalid")

    def test_modify(self):
        """
        Test function for modifying a film
        """
        self.__film_repo.add(self.__film_)

        self.__film_repo.modify(self.__film2)

        films = self.__film_repo.get_all()
        self.assertEqual(films[0], self.__film2)

        film3 = Film(6, "ss", "sdd", "ddd")
        with self.assertRaises(RepoException) as cm:
            self.__film_repo.modify(film3)
        self.assertEqual(str(cm.exception), "Id invalid")

    def test_clear(self):
        """
        Test function for clear
        """
        self.__film_repo.add(self.__film)

        self.assertEqual(self.__film_repo.size(), 1)
        self.__film_repo.clear()
        self.assertEqual(self.__film_repo.size(), 0)


if __name__ == '__main__':
    unittest.main()
