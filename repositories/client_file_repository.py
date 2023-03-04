"""
Class definition of a Client File Repository
"""
from domain.entities import Client
from repositories.client_repository import ClientRepository


class ClientFileRepository(ClientRepository):
    """
    Manages a list of Client instances and provides basic CRUD operations (with file I/O)
    """
    def __init__(self, filename):
        """
        Initializes a blank client file repository using the given file path

        :param filename: string
        """
        super().__init__()
        self.__filename = filename

    def __load_from_file(self):
        """
        Loads the clients from the file into the _clients list
        """
        self._clients = []
        try:
            with open(self.__filename, "r") as fh:
                for line in fh:
                    elements = line.strip().split(";")
                    id = int(elements[0])
                    name = elements[1]
                    cnp = int(elements[2])

                    client = Client(id, name, cnp)
                    self._clients.append(client)
        except IOError:
            return  # in case of file error, the _clients list will be empty

    def __save_to_file(self):
        """
        Saves the _clients list to the file
        """
        with open(self.__filename, "w") as fh:
            for client in self._clients:
                str_client = f"{client.get_id()};{client.get_name()};{client.get_cnp()}\n"
                fh.write(str_client)

    def size(self):
        """
        Computes the size of the repository (number of clients stored)

        :return: size, an integer
        """
        self.__load_from_file()
        return super().size()

    def add(self, client):
        """
        Adds a Client object to the repository

        :param client: Client object
        :raises RepoException: if an object with the same id is already stored in the repository
        """
        self.__load_from_file()
        super().add(client)
        self.__save_to_file()

    def get_all(self):
        """
        Provides access to all the objects in the repository

        :return: a list of all objects
        """
        self.__load_from_file()
        return super().get_all()

    def find(self, id):
        """
        Finds a client by id from the repository

        :param id: an integer
        :return: the found client
        :raises RepoException: if the id is invalid or the client with the given id doesn't exist
        """
        self.__load_from_file()
        return super().find(id)

    def modify(self, client):
        """
        Modifies a client from the repository using another instance

        :param client: a Client object containing the new values, but with the same id
        :raises RepoException: if the id is invalid or the client with the given id doesn't exist
        """
        self.__load_from_file()
        super().modify(client)
        self.__save_to_file()

    def delete(self, id):
        """
        Deletes the client with the id provided from the repository

        :param id: an integer
        :raises RepoException: if the client identified by the id is not in the repository
        """
        self.__load_from_file()
        super().delete(id)
        self.__save_to_file()

    def clear(self):
        """
        Clears the repository
        """
        super().clear()
        self.__save_to_file()
