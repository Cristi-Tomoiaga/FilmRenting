"""
Class definitions of the data transfer objects (DTOs) in the project
"""


class ClientDTO:
    """
    DTO for a client with a list of films rented
    """
    def __init__(self, id, name):
        """
        Initializes the object

        :param id: integer
        :param name: string
        """
        self.__id = id
        self.__name = name
        self.__films = []
        self.__num_films = 0

    def get_id(self):
        """
        Getter for id

        :return: id, integer
        """
        return self.__id

    def get_name(self):
        """
        Getter for name

        :return: name, string
        """
        return self.__name

    def get_num_films(self):
        """
        Gets the number of films in the list

        :return: num_films, integer
        """
        return self.__num_films

    def get_films(self):
        """
        Getter for films

        :return: films, list
        """
        return self.__films[:]

    def add_film(self, film):
        """
        Adds a Film object to the list of films

        :param film: Film object
        """
        if film not in self.__films:  # make sure we don't store duplicates
            self.__films.append(film)

        self.__num_films += 1  # but count them to the total

    def __str__(self):
        """
        Gives the string representation for the object

        :return: string
        """
        string = f"Id: {self.get_id()}, Nume: {self.get_name()} - {self.get_num_films()}:\n"
        for film in self.get_films():
            string += f"\tId: {film.get_id()}, Titlu: {film.get_title()}\n"

        return string


class FilmDTO:
    """
    DTO for a film with the number of transactions made with that film
    """
    def __init__(self, id, title):
        """
        Initializes the object

        :param id: integer
        :param title: string
        """
        self.__id = id
        self.__title = title
        self.__count = 0

    def get_id(self):
        """
        Getter for id

        :return: id, integer
        """
        return self.__id

    def get_title(self):
        """
        Getter for title

        :return: title, string
        """
        return self.__title

    def get_num_rent(self):
        """
        Getter for count (number of rents)

        :return: count, integer
        """
        return self.__count

    def inc_num_rent(self):
        """
        Increments count
        """
        self.__count += 1

    def __str__(self):
        """
        Gives the string representation for the object

        :return: string
        """
        return f"Id: {self.get_id()}, Titlu: {self.get_title()} - {self.get_num_rent()}\n"
