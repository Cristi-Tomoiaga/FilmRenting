"""
Class definition of the Client Service
"""
import random

from domain.entities import Client
from domain.exceptions import ValidatorException, RepoException
from utils.random_generation import generate_random_string, generate_random_cnp


class ClientService:
    """
    Manages use cases for CRUD operations on a lists of clients
    """
    def __init__(self, client_repo, client_validator):
        """
        Initializes the Client Service
        :param client_repo: ClientRepository object
        :param client_validator: ClientValidator object
        """
        self.__repo = client_repo
        self.__validator = client_validator

    def add_client(self, id, name, cnp):
        """
        Implements the use case of adding a client

        :param id: integer
        :param name: string
        :param cnp: integer
        :return: Client object
        :raises ValidatorException: if the values provided are invalid
        :raises RepoException: if there is already another object with the same id in the repository
        """
        client = Client(id, name, cnp)

        self.__validator.validate(client)

        self.__repo.add(client)

        return client

    def get_all_clients(self):
        """
        Implements the use case of printing the current clients in the repository

        :return: a list of string representations for the clients in the repository
        """
        clients = self.__repo.get_all()

        str_clients = []
        for client in clients:
            str_clients.append(str(client))

        return str_clients

    def modify_client(self, id, name, cnp):
        """
        Implements the use case of modifying a client identified by id

        :param id: integer
        :param name: string
        :param cnp: integer
        :return: the modified Client object
        :raises RepoException: if the id is invalid or the client with the given id doesn't exist
        :raises ValidatorException: if the values provided are invalid
        """
        new_client = Client(id, name, cnp)

        self.__validator.validate(new_client)

        self.__repo.modify(new_client)

        return new_client

    def delete_client(self, id):
        """
        Implements the use case of deleting a client

        :param id: an integer
        :raises RepoException: if the id is invalid
        """
        self.__repo.delete(id)

    def find_client_by_cnp(self, cnp, i=0):
        """
        Implements the use case of finding a client by cnp from the repository

        :param cnp: integer
        :param i: integer, current iterating position
        :return: the found client
        :raises RepoException: if the cnp is invalid or the client with the given cnp doesn't exist
        """
        if i >= self.__repo.size():  # client not found
            raise RepoException("CNP invalid")

        clients = self.__repo.get_all()
        if clients[i].get_cnp() == cnp:
            return clients[i]

        return self.find_client_by_cnp(cnp, i + 1)

    def find_client_by_name(self, name):
        """
        Implements the use case of finding one or more clients by name from the repository

        :param name: string
        :return: a list of clients
        """
        clients = self.__repo.get_all()
        result = []

        for client in clients:
            if name in client.get_name():
                result.append(client)

        return result

    def generate_clients_random(self, x):
        """
        Generates X random Client objects
        :param x: integer
        """
        no_of_gen_items = 0
        self.__repo.clear()

        while no_of_gen_items < x:
            id = random.randint(1, x)
            name = generate_random_string(random.randint(1, 10))
            cnp = generate_random_cnp()

            try:
                self.add_client(id, name, cnp)
                no_of_gen_items += 1
            except (ValidatorException, RepoException):
                pass
