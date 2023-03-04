"""
Class definition of the Transaction Service
"""
import random
from functools import cmp_to_key
from math import ceil

from domain.datatransfer import ClientDTO, FilmDTO
from domain.entities import Transaction
from domain.exceptions import RepoException, ValidatorException
from utils.sorting_algs import Sorting, SortingMethod


class TransactionService:
    """
    Manages use cases for CRUD operations on a lists of transactions
    """
    def __init__(self, transaction_repo, transaction_validator, film_repo, client_repo):
        """
        Initializes the Transaction Service

        :param transaction_repo: TransactionRepository object
        :param transaction_validator: TransactionValidator object
        :param film_repo: FilmRepository object
        :param client_repo: ClientRepository object
        """
        self.__repo = transaction_repo
        self.__validator = transaction_validator
        self.__film_repo = film_repo
        self.__client_repo = client_repo

    def rent_film_to_client(self, id_transaction, id_film, id_client):
        """
        Implements the use case of renting a film to a client

        :param id_transaction: integer
        :param id_film: integer
        :param id_client: integer
        :raises RepoException: if the id_film or id_client are invalid, a transaction with the same id already exists or the film is already rented
        :raises ValidatorException: if id_transaction is invalid
        """
        film = self.__film_repo.find(id_film)

        if self.__repo.is_film_rented(film):
            raise RepoException("Filmul este deja inchiriat")

        client = self.__client_repo.find(id_client)

        tr = Transaction(id_transaction, film, client)

        self.__validator.validate(tr)

        self.__repo.add(tr)

    def return_film_from_client(self, id_film, id_client):
        """
        Implements the use case of returning a film from a client

        :param id_film: integer
        :param id_client: integer
        :raises RepoException: if the ids provided are invalid, the transaction was already returned or it didn't exist
        """
        film = self.__film_repo.find(id_film)

        client = self.__film_repo.find(id_client)

        self.__repo.return_transaction(film, client)

    def report_clients_by_name(self):
        """
        Generates a list of ClientDTO objects sorted by the client name

        :return: the list (with the string representation of the objects)
        """
        clients = self.__client_repo.get_all()

        report = []
        for client in clients:
            trs = self.__repo.get_all_for_client(client)

            client_dto = ClientDTO(client.get_id(), client.get_name())
            for tr in trs:
                client_dto.add_film(tr.get_film())

            report.append(client_dto)

        report = Sorting.sorted(report, key=lambda clt_dto: clt_dto.get_name(), method=SortingMethod.MERGE_SORT)

        str_report = list(map(lambda cl_dto: str(cl_dto), report))  # convert all the objects to their string version

        return str_report

    def report_clients_by_number(self):
        """
        Generates a list of ClientDTO objects sorted descending by the number of rented films for each client

        :return: the list (with the string representation of the objects)
        """
        clients = self.__client_repo.get_all()

        report = []
        for client in clients:
            trs = self.__repo.get_all_for_client(client)

            client_dto = ClientDTO(client.get_id(), client.get_name())
            for tr in trs:
                client_dto.add_film(tr.get_film())

            report.append(client_dto)

        def cmp_client_dto(clt_dto1, clt_dto2):
            """
            Compares two ClientDTO objects on num_films and then on name

            :param clt_dto1: ClientDTO
            :param clt_dto2: ClientDTO
            :return: -1 if less, 0 if equal or +1 if greater
            """
            if clt_dto1.get_num_films() < clt_dto2.get_num_films():
                return -1
            elif clt_dto1.get_num_films() > clt_dto2.get_num_films():
                return 1
            else:
                if clt_dto1.get_name() < clt_dto2.get_name():
                    return -1
                elif clt_dto1.get_name() > clt_dto2.get_name():
                    return 1
                else:
                    return 0

        report = Sorting.sorted(report, key=cmp_to_key(cmp_client_dto), reverse=True, method=SortingMethod.BINGO_SORT)

        str_report = list(map(lambda cl_dto: str(cl_dto), report))  # convert all the objects to their string version

        return str_report

    def report_first_clients(self):
        """
        Generates a list of the first 30% ClientDTO objects from the sorted in descending order by
        the number of rented films for each client

        :return: the list (with the string representation of the objects)
        """
        str_report = self.report_clients_by_number()

        limit = ceil(0.3 * len(str_report))  # 30% of the clients rounded up (so we can use it as an index limit)

        return str_report[:limit]

    def report_films(self):
        """
        Generates a list of FilmDTO objects sorted descending by the number of clients that rented each film

        :return: the list (with the string representation of the objects)
        """
        films = self.__film_repo.get_all()

        report = []
        for film in films:
            trs = self.__repo.get_all_for_film(film)

            film_dto = FilmDTO(film.get_id(), film.get_title())
            for _ in trs:
                film_dto.inc_num_rent()

            report.append(film_dto)

        report = Sorting.sorted(report, key=lambda fl_dto: fl_dto.get_num_rent(), reverse=True, method=SortingMethod.MERGE_SORT)

        str_report = list(map(lambda fl_dto: str(fl_dto), report))  # convert all the objects to their string version

        return str_report

    def report_last_films(self, prefix):
        """
        Generates a list of FilmDTO objects with titles that start with a given prefix, limits to last 50% films (ordered by num_rent)
        and then sorts it by title

        :param prefix: string
        :return: the list (with the string representation of the objects)
        """
        films = self.__film_repo.get_all()

        filtered_films = list(filter(lambda flm: flm.get_title().startswith(prefix), films))  # filter the films with prefix

        report = []
        for film in filtered_films:
            trs = self.__repo.get_all_for_film(film)

            film_dto = FilmDTO(film.get_id(), film.get_title())
            for _ in trs:
                film_dto.inc_num_rent()

            report.append(film_dto)

        report = Sorting.sorted(report, key=lambda flm_dto: flm_dto.get_num_rent(), method=SortingMethod.BINGO_SORT)  # sorted in ascending order by num_rent

        # now the last 50% of rented films is the same with the first 50% here
        limit = ceil(0.5 * len(report))  # first 50% of the films rounded up (so we can use it as an index limit)

        report = report[:limit]

        report = Sorting.sorted(report, key=lambda flm_dto: flm_dto.get_title(), method=SortingMethod.MERGE_SORT)  # sorted in ascending order by title

        str_report = list(map(lambda flm_dto: str(flm_dto), report))

        return str_report

    def generate_transactions_random(self, x, tweak=False):
        """
        Generates X random Transaction objects
        :param x: integer
        :param tweak: boolean, if True makes the generation more diverse
        """
        no_of_gen_items = 0
        self.__repo.clear()

        while no_of_gen_items < x:
            id_transaction = random.randint(1, x)
            id_film = random.randint(1, self.__film_repo.size())
            id_client = random.randint(1, self.__client_repo.size())

            try:
                self.rent_film_to_client(id_transaction, id_film, id_client)

                if tweak:
                    chance = random.random()
                    if chance < 0.4:
                        self.return_film_from_client(id_film, id_client)

                no_of_gen_items += 1
            except (ValidatorException, RepoException):
                pass
