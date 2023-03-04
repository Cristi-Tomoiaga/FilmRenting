"""
Class definition of a Transaction Repository
"""
from domain.exceptions import RepoException


class TransactionRepository:
    """
    Manages a list of Transaction instances and provides basic CRUD operations
    """
    def __init__(self):
        """
        Initializes a blank list of transactions in the repository
        """
        self._transactions = []

    def size(self):
        """
        Computes the size of the repository (number of transactions stored)

        :return: size, an integer
        """
        return len(self._transactions)

    def add(self, transaction):
        """
        Adds a Transaction object to the repository

        :param transaction: Transaction object
        :raises RepoException: if an object with the same id is already stored in the repository
        """
        if transaction in self._transactions:
            raise RepoException("Id existent pentru inchiriere")

        self._transactions.append(transaction)

    def return_transaction(self, film, client):
        """
        Returns a Transaction object based on the film and client objects provided

        :param film: Film Object
        :param client: Client Object
        :raises RepoException: if the transaction doesn't exist
        """
        tr = self.find_by_film_client(film, client)
        tr.return_transaction()

    def find_by_film_client(self, film, client):
        """
        Finds a transaction with the given film and client object, which has not been returned

        :param film: Film object
        :param client: Client Object
        :return: the found transaction
        :raises RepoException: if no transactions were found
        """
        found = False

        for tr in self._transactions:
            if tr.get_film() == film and tr.get_client() == client and not tr.is_returned():
                found = True
                return tr

        if not found:
            raise RepoException("Inchiriere inexistenta")

    def is_film_rented(self, film):
        """
        Checks if there is a transaction with the given film, which has not been returned

        :param film: Film object
        :return: True if found, False otherwise
        """
        found = False

        for tr in self._transactions:
            if tr.get_film() == film and not tr.is_returned():
                found = True

        return found

    def get_all_for_client(self, client):
        """
        Gets all the transactions that the client made

        :param client: Client object
        :return: the list of Transaction objects
        """
        trs = []

        for tr in self._transactions:
            if tr.get_client() == client:
                trs.append(tr)

        return trs

    def get_all_for_film(self, film):
        """
        Gets all the transactions for the given film

        :param film: Film object
        :return: the list of Transaction objects
        """
        trs = []

        for tr in self._transactions:
            if tr.get_film() == film:
                trs.append(tr)
        return trs

    def clear(self):
        """
        Clears the repository
        """
        self._transactions.clear()
