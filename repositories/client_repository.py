"""
Class definition of a Client Repository
"""
from domain.exceptions import RepoException


class ClientRepository:
    """
    Manages a list of Client instances and provides basic CRUD operations
    """
    def __init__(self):
        """
        Initializes a blank list of clients in the repository
        """
        self._clients = []

    def size(self):
        """
        Computes the size of the repository (number of clients stored)

        :return: size, an integer
        """
        return len(self._clients)

    def add(self, client):
        """
        Adds a Client object to the repository

        :param client: Client object
        :raises RepoException: if an object with the same id is already stored in the repository
        """
        if client in self._clients:
            raise RepoException("Id existent")

        self._clients.append(client)

    def get_all(self):
        """
        Provides access to all the objects in the repository

        :return: a list of all objects
        """
        return self._clients

    def find(self, id):
        """
        Finds a client by id from the repository

        :param id: an integer
        :return: the found client
        :raises RepoException: if the id is invalid or the client with the given id doesn't exist
        """
        found = False

        for client in self._clients:
            if client.get_id() == id:
                found = True
                return client

        if not found:
            raise RepoException("Id invalid")

    def modify(self, client):
        """
        Modifies a client from the repository using another instance

        :param client: a Client object containing the new values, but with the same id
        :raises RepoException: if the id is invalid or the cient with the given id doesn't exist
        """
        found_client = self.find(client.get_id())

        found_client.set_name(client.get_name())
        found_client.set_cnp(client.get_cnp())

    def delete(self, id):
        """
        Deletes the client with the id provided from the repository

        :param id: an integer
        :raises RepoException: if the client identified by the id is not in the repository
        """
        found = False

        for i in range(0, self.size()):  # search for the film identified by id
            if self._clients[i].get_id() == id:
                found = True
                del self._clients[i]  # if found, delete it from the list
                return  # no need to iterate further

        if not found:
            raise RepoException("Id invalid")

    def clear(self):
        """
        Clears the repository
        """
        self._clients.clear()
