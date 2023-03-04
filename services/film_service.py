"""
Class definition of the Film Service
"""
import random

from domain.entities import Film
from domain.exceptions import ValidatorException, RepoException
from utils.random_generation import generate_random_string


class FilmService:
    """
    Manages use cases for CRUD operations on a lists of films
    """
    def __init__(self, film_repo, film_validator):
        """
        Initializes the film service

        :param film_repo: FilmRepository object
        :param film_validator: FilmValidator object
        """
        self.__repo = film_repo
        self.__validator = film_validator

    def add_film(self, id, title, description, genre):
        """
        Implements the use case of adding a film

        :param id: integer
        :param title: string
        :param description: string
        :param genre: string
        :return: the new Film object added to the repository
        :raises RepoException: if there is another Film object with the same id in the repository
        :raises ValidatorException: if the values provided are invalid
        """
        film = Film(id, title, description, genre)

        self.__validator.validate(film)

        self.__repo.add(film)

        return film

    def modify_film(self, id, title, description, genre):
        """
        Implements the use case of modifying a film identified by id

        :param id: integer
        :param title: string
        :param description: string
        :param genre: string
        :return: the modified Film object
        :raises RepoException: if the id is invalid or the film with the given id doesn't exist
        :raises ValidatorException: if the values provided are invalid
        """
        new_film = Film(id, title, description, genre)

        self.__validator.validate(new_film)

        self.__repo.modify(new_film)

        return new_film

    def get_all_films(self):
        """
        Implements the use case of printing the current films in the repository

        :return: a list of string representations for the films in the repository
        """
        films = self.__repo.get_all()

        str_films = []
        for film in films:
            str_films.append(str(film))

        return str_films

    def filter_film_with_prefix(self, prefix):
        """
        Implements the use case of filtering the list of films by a prefix

        :param prefix: a string
        :return: a list of string representations for the filtered repository
        """
        films = self.__repo.get_all()

        str_films_filtered = []
        for film in films:
            if film.get_title().startswith(prefix):
                str_films_filtered.append(str(film))

        return str_films_filtered

    def delete_film(self, id):
        """
        Implements the use case of deleting a film
        :param id: an integer
        :raises RepoException: if the id is invalid
        """
        self.__repo.delete(id)

    def find_film_by_title(self, title, i=0):
        """
        Implements the use case of finding one or more films by title from the repository

        :param title: string
        :param i: integer, current iterating position
        :return: a list of films
        """
        if i >= self.__repo.size():
            return []

        films = self.__repo.get_all()
        if title in films[i].get_title():
            return [films[i]] + self.find_film_by_title(title, i + 1)

        return self.find_film_by_title(title, i + 1)

    def generate_films_random(self, x):
        """
        Generates X random Film objects
        :param x: integer
        """
        no_of_gen_items = 0
        self.__repo.clear()

        while no_of_gen_items < x:
            id = random.randint(1, x)
            title = generate_random_string(random.randint(1, 10))
            description = generate_random_string(random.randint(1, 20))
            genre = generate_random_string(random.randint(1, 5))

            try:
                self.add_film(id, title, description, genre)
                no_of_gen_items += 1
            except (ValidatorException, RepoException):
                pass
