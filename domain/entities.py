"""
Class definitions of the entities in the project
"""
from datetime import datetime


class Film:
    """
    Abstract data type for a film

    Domain:
        id - integer
        title, description, genre - strings
    """
    def __init__(self, id, title, description, genre):
        """
        Constructor for Film class

        :param id: integer
        :param title: string
        :param description: string
        :param genre: string
        """
        self.__id = id
        self.__title = title
        self.__description = description
        self.__genre = genre

    def get_id(self):
        """
        Getter for id

        :return: id - integer
        """
        return self.__id

    def get_title(self):
        """
        Getter for title

        :return: title - string
        """
        return self.__title

    def set_title(self, title):
        """
        Setter for title

        :param title: a string
        """
        self.__title = title

    def get_description(self):
        """
        Getter for description

        :return: description - string
        """
        return self.__description

    def set_description(self, description):
        """
        Setter for description
        :param description: a string
        """
        self.__description = description

    def get_genre(self):
        """
        Getter for genre

        :return: genre - string
        """
        return self.__genre

    def set_genre(self, genre):
        """
        Setter for genre
        :param genre: a string
        """
        self.__genre = genre

    def __eq__(self, other):
        """
        Verify if the id of self is equal to the id of other

        :param other: Film object
        :return: True if equal, False otherwise
        """
        return self.get_id() == other.get_id()

    def __str__(self):
        """
        Builds the string representation for the current object

        :return: the string representation
        """
        string = f"{self.get_id()}. {self.get_title()}, {self.get_description()}, {self.get_genre()}"
        return string


class Client:
    """
    Abstract data type for a client

    Domain:
        id, cnp - integers
        name - string
    """
    def __init__(self, id, name, cnp):
        """
        Constructor for Client class

        :param id: integer
        :param name: string
        :param cnp: integer
        """
        self.__id = id
        self.__name = name
        self.__cnp = cnp

    def get_id(self):
        """
        Getter method for id

        :return: id, an integer
        """
        return self.__id

    def get_name(self):
        """
        Getter method for name

        :return: name, a string
        """
        return self.__name

    def get_cnp(self):
        """
        Getter method for cnp

        :return: cnp, an integer
        """
        return self.__cnp

    def set_name(self, name):
        """
        Setter method for name

        :param name: string
        """
        self.__name = name

    def set_cnp(self, cnp):
        """
        Setter method for cnp
        :param cnp: integer
        """
        self.__cnp = cnp

    def __eq__(self, other):
        """
        Verify if two clients are equal, i.e. they have the same id

        :param other: Client object
        :return: True if equal self is equal to other, False otherwise
        """
        return self.get_id() == other.get_id()

    def __str__(self):
        """
        Builds the string representation of a Client object

        :return: the string representation
        """
        string = f"Id: {self.get_id()}, Nume: {self.get_name()}, CNP: {self.get_cnp()}"

        return string


class Transaction:
    """
    Abstract data type for a transaction

    Domain:
        id - integer
        film - Film object
        client - Client object
        date - datetime
        returned - boolean
    """
    def __init__(self, id, film, client):
        """
        Constructor for Transaction

        :param id: integer
        :param film: Film object
        :param client: Client object
        """
        self.__id = id
        self.__film = film
        self.__client = client
        self.__date = datetime.now()  # save the date and time of the instantiation
        self.__returned = False  # a newly created transaction is not yet returned

    def get_id(self):
        """
        Getter method for id

        :return: id, an integer
        """
        return self.__id

    def get_film(self):
        """
        Getter method for film

        :return: a Film object
        """
        return self.__film

    def get_client(self):
        """
        Getter method for client

        :return: a Client object
        """
        return self.__client

    def get_date(self):
        """
        Getter method for date

        :return: a datetime object
        """
        return self.__date

    def set_date(self, date):
        """
        Setter method for date
        :param date: a datetime object
        """
        self.__date = date

    def is_returned(self):
        """
        Getter method for returned

        :return: returned, boolean
        """
        return self.__returned

    def set_returned(self, val):
        """
        Setter method for returned
        :param val: boolean value
        """
        self.__returned = val

    def return_transaction(self):
        """
        Sets the returned field to True
        """
        self.__returned = True

    def __eq__(self, other):
        """
        Verify if two transactions are equal
        :param other: Transaction object
        :return: True if equal, False otherwise
        """
        return self.get_id() == other.get_id() \
            and self.get_film() == other.get_film() and self.get_client() == other.get_client()

    def __str__(self):
        """
        Builds the string representation of a Transaction object
        """
        string = f"Id_tranzactie: {self.get_id()}, Id_film: {self.get_film().get_id()}, Id_client: {self.get_client().get_id()}, " \
                 f"Data: {self.get_date().strftime('%d.%m.%Y')}, Ora: {self.get_date().strftime('%H:%M')}, Returnat: {self.is_returned()}"

        return string
