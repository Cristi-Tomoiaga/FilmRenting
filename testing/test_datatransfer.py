"""
Test cases for datatransfer module
"""
import unittest

from domain.datatransfer import ClientDTO, FilmDTO
from domain.entities import Film


class TestCaseClientDTO(unittest.TestCase):
    def setUp(self):
        self.__cldto = ClientDTO(1, "John Doe")
        self.__flm = Film(1, "Film1", "Desc1", "Gen1")
        self.__flm2 = Film(2, "Film2", "Desc2", "Gen2")

    def test_create(self):
        """
        Test function for the creation of ClientDTO
        """
        self.assertEqual(self.__cldto.get_id(), 1)
        self.assertEqual(self.__cldto.get_name(), "John Doe")

        self.assertEqual(self.__cldto.get_num_films(), 0)
        self.__cldto.add_film(self.__flm)
        self.assertEqual(self.__cldto.get_num_films(), 1)
        self.__cldto.add_film(self.__flm)
        self.assertEqual(self.__cldto.get_num_films(), 2)
        films = self.__cldto.get_films()
        self.assertEqual(films, [self.__flm])

        self.__cldto.add_film(self.__flm2)
        self.assertEqual(self.__cldto.get_num_films(), 3)

    def test_string(self):
        """
        Test function for string representation of ClientDTO
        """
        self.assertEqual(str(self.__cldto), "Id: 1, Nume: John Doe - 0:\n")

        self.__cldto.add_film(self.__flm)
        self.assertEqual(str(self.__cldto), "Id: 1, Nume: John Doe - 1:\n\tId: 1, Titlu: Film1\n")


class TestCaseFilmDTO(unittest.TestCase):
    def setUp(self):
        self.__flmdto = FilmDTO(1, "Film1")

    def test_create(self):
        """
        Test function for the creation of FilmDTO
        """
        self.assertEqual(self.__flmdto.get_id(), 1)
        self.assertEqual(self.__flmdto.get_title(), "Film1")

        self.assertEqual(self.__flmdto.get_num_rent(), 0)
        self.__flmdto.inc_num_rent()
        self.assertEqual(self.__flmdto.get_num_rent(), 1)

    def test_string(self):
        """
        Test function for string representation fo FilmDTO
        """
        self.assertEqual(str(self.__flmdto), "Id: 1, Titlu: Film1 - 0\n")

        self.__flmdto.inc_num_rent()
        self.assertEqual(str(self.__flmdto), "Id: 1, Titlu: Film1 - 1\n")


if __name__ == '__main__':
    unittest.main()
