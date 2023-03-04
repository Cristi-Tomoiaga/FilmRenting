"""
Class definition of a Film File Repository
"""
from domain.entities import Film
from repositories.film_repository import FilmRepository


class FilmFileRepository(FilmRepository):
    """
    Manages a list of Film instances and provides basic CRUD operations (with file I/O)
    """
    def __init__(self, filename):
        """
        Initializes a blank film file repository using the given file path

        :param filename: string
        """
        super().__init__()
        self.__filename = filename

    def __load_from_file(self):
        """
        Loads the films from the file into the _films list
        """
        self._films = []
        try:
            with open(self.__filename, "r") as fh:
                for line in fh:
                    elements = line.strip().split(";")
                    id = int(elements[0])
                    title = elements[1]
                    description = elements[2]
                    genre = elements[3]

                    film = Film(id, title, description, genre)
                    self._films.append(film)
        except IOError:
            return  # in case of file error, the _films list will be empty

    def __save_to_file(self):
        """
        Saves the _films list to the file
        """
        with open(self.__filename, "w") as fh:
            for film in self._films:
                str_film = f"{film.get_id()};{film.get_title()};{film.get_description()};{film.get_genre()}\n"
                fh.write(str_film)

    def add(self, film):
        """
        Adds a new film instance to the repository

        :param film: Film object
        :raises RepoException: if there is another Film object with the same id in the repository
        """
        self.__load_from_file()
        super().add(film)
        self.__save_to_file()

    def find(self, id):
        """
        Finds a film by id from the repository

        :param id: an integer
        :return: the found film
        :raises RepoException: if the id is invalid or the film with the given id doesn't exist
        """
        self.__load_from_file()
        return super().find(id)

    def modify(self, film):
        """
        Modifies a film from the repository using another instance

        :param film: a Film object containing the new values, but with the same id
        :raises RepoException: if the id is invalid or the film with the given id doesn't exist
        """
        self.__load_from_file()
        super().modify(film)
        self.__save_to_file()

    def get_all(self):
        """
        Provides access to all the objects in the repository

        :return: a list of all objects
        """
        self.__load_from_file()
        return super().get_all()

    def delete(self, id):
        """
        Deletes the film with the id provided from the repository

        :param id: an integer
        :raises RepoException: if the film identified by the id is not in the repository
        """
        self.__load_from_file()
        super().delete(id)
        self.__save_to_file()

    def size(self):
        """
        Computes the number of objects in the repository

        :return: that number
        """
        self.__load_from_file()
        return super().size()

    def clear(self):
        """
        Clears the repository
        """
        super().clear()
        self.__save_to_file()
