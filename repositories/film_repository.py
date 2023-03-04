"""
Class definition of a Film repository
"""
from domain.exceptions import RepoException


class FilmRepository:
    """
    Manages a list of Film instances and provides basic CRUD operations
    """
    def __init__(self):
        """
        Initializes a blank list of films in the repository
        """
        self._films = []

    def add(self, film):
        """
        Adds a new film instance to the repository

        :param film: Film object
        :raises RepoException: if there is another Film object with the same id in the repository
        """
        if film in self._films:
            raise RepoException("Id existent")

        self._films.append(film)

    def find(self, id):
        """
        Finds a film by id from the repository

        :param id: an integer
        :return: the found film
        :raises RepoException: if the id is invalid or the film with the given id doesn't exist
        """
        found = False
        for film in self._films:
            if film.get_id() == id:
                found = True
                return film

        if not found:
            raise RepoException("Id invalid")

    def modify(self, film):
        """
        Modifies a film from the repository using another instance

        :param film: a Film object containing the new values, but with the same id
        :raises RepoException: if the id is invalid or the film with the given id doesn't exist
        """
        found_film = self.find(film.get_id())

        found_film.set_title(film.get_title())
        found_film.set_description(film.get_description())
        found_film.set_genre(film.get_genre())

    def get_all(self):
        """
        Provides access to all the objects in the repository

        :return: a list of all objects
        """
        return self._films

    def delete(self, id):
        """
        Deletes the film with the id provided from the repository

        :param id: an integer
        :raises RepoException: if the film identified by the id is not in the repository
        """
        found = False

        for i in range(0, self.size()):  # search for the film identified by id
            if self._films[i].get_id() == id:
                found = True
                del self._films[i]  # if found, delete it from the list
                return  # no need to iterate further

        if not found:
            raise RepoException("Id invalid")

    def size(self):
        """
        Computes the number of objects in the repository

        :return: that number
        """
        return len(self._films)

    def clear(self):
        """
        Clears the repository
        """
        self._films.clear()
