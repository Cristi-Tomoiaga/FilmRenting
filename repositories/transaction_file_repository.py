"""
Class definition of a Transaction File Repository
"""
import datetime

from domain.entities import Transaction
from repositories.transaction_repository import TransactionRepository


class TransactionFileRepository(TransactionRepository):
    """
    Manages a list of Transaction instances and provides basic CRUD operations (with file I/O)
    """
    def __init__(self, filename, film_repo, client_repo):
        """
        Initializes a blank transaction file repository using the given file path

        :param filename: string
        :param film_repo: FilmRepository object
        :param client_repo: ClientRepository object
        """
        super().__init__()
        self.__filename = filename
        self.__fl_repo = film_repo
        self.__cl_repo = client_repo

    def __load_from_file(self):
        """
        Loads the transactions from the file into the _transactions list
        """
        self._transactions = []
        try:
            with open(self.__filename, "r") as fh:
                for line in fh:
                    elements = line.strip().split(";")
                    id = int(elements[0])
                    id_film = int(elements[1])
                    film = self.__fl_repo.find(id_film)
                    id_client = int(elements[2])
                    client = self.__cl_repo.find(id_client)
                    returned = (elements[3] == "True")
                    date = datetime.datetime.strptime(elements[4], "%d.%m.%Y %H:%M")

                    tr = Transaction(id, film, client)
                    tr.set_returned(returned)
                    tr.set_date(date)

                    self._transactions.append(tr)
        except IOError:
            return  # in case of file error, the _transactions list will be empty

    def __save_to_file(self):
        """
        Saves the _transactions list to the file
        """
        with open(self.__filename, "w") as fh:
            for tr in self._transactions:
                str_tr = f"{tr.get_id()};{tr.get_film().get_id()};{tr.get_client().get_id()};{tr.is_returned()};{tr.get_date().strftime('%d.%m.%Y %H:%M')}\n"
                fh.write(str_tr)

    def size(self):
        """
        Computes the size of the repository (number of transactions stored)

        :return: size, an integer
        """
        self.__load_from_file()
        return super().size()

    def add(self, transaction):
        """
        Adds a Transaction object to the repository

        :param transaction: Transaction object
        :raises RepoException: if an object with the same id is already stored in the repository
        """
        self.__load_from_file()
        super().add(transaction)
        self.__save_to_file()

    def return_transaction(self, film, client):
        """
        Returns a Transaction object based on the film and client objects provided

        :param film: Film Object
        :param client: Client Object
        :raises RepoException: if the transaction doesn't exist
        """
        self.__load_from_file()
        super().return_transaction(film, client)
        self.__save_to_file()

    def find_by_film_client(self, film, client):
        """
        Finds a transaction with the given film and client object, which has not been returned

        :param film: Film object
        :param client: Client Object
        :return: the found transaction
        :raises RepoException: if no transactions were found
        """
        self.__load_from_file()
        return super().find_by_film_client(film, client)

    def is_film_rented(self, film):
        """
        Checks if there is a transaction with the given film, which has not been returned

        :param film: Film object
        :return: True if found, False otherwise
        """
        self.__load_from_file()
        return super().is_film_rented(film)

    def get_all_for_client(self, client):
        """
        Gets all the transactions that the client made

        :param client: Client object
        :return: the list of Transaction objects
        """
        self.__load_from_file()
        return super().get_all_for_client(client)

    def get_all_for_film(self, film):
        """
        Gets all the transactions for the given film

        :param film: Film object
        :return: the list of Transaction objects
        """
        self.__load_from_file()
        return super().get_all_for_film(film)

    def clear(self):
        """
        Clears the repository
        """
        super().clear()
        self.__save_to_file()
