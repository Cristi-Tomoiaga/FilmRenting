"""
Implementation of a menu-based console application
"""
from domain.exceptions import RepoException, ValidatorException


class Console:
    """
    Manages a menu application and handles events accordingly
    """

    def __init__(self, film_srv, client_srv, transaction_srv):
        """
        Initializes the console UI

        :param film_srv: FilmService object
        :param client_srv: ClientService object
        :param transaction_srv: TransactionService object
        """
        self.__film_service = film_srv
        self.__client_service = client_srv
        self.__transaction_service = transaction_srv

    def __get_command(self):
        """
        Gets input and returns the given command

        :return: the command, a string
        """

        cmd = input("$ ").strip()

        return cmd

    def __get_all_commands(self):
        """
        Builds a dictionary that associates commands with functions from this class

        :return: the dictionary
        """
        return {
            "add_film": self.__add_film_ui,
            "add_client": self.__add_client_ui,
            "modify_film": self.__modify_film_ui,
            "modify_client": self.__modify_client_ui,
            "delete_film": self.__delete_film_ui,
            "delete_client": self.__delete_client_ui,
            "print_films": self.__print_films_ui,
            "print_clients": self.__print_clients_ui,
            "find_client_by_cnp": self.__find_client_by_cnp_ui,
            "find_client_by_name": self.__find_client_by_name_ui,
            "find_film_by_title": self.__find_film_by_title_ui,
            "filter_film_with_prefix": self.__filter_film_with_prefix_ui,
            "report_clients_by_name": self.__report_clients_by_name_ui,
            "report_clients_by_number": self.__report_clients_by_number_ui,
            "report_films": self.__report_films_ui,
            "report_first_clients": self.__report_first_clients_ui,
            "report_last_films": self.__report_last_films,
            "rent": self.__rent_ui,
            "return": self.__return_ui,
            "random": self.__random_ui,
            "help": self.__help_ui,
            "quit": exit
        }

    def __add_film_ui(self):
        """
        Adds a new film to the repository
        """
        try:
            id = int(input("Introduce un id: ").strip())
            title = input("Introduce un titlu: ").strip()
            description = input("Introduce o descriere: ").strip()
            genre = input("Introduce un gen: ").strip()

            film = self.__film_service.add_film(id, title, description, genre)

            print(f"Filmul cu id-ul {film.get_id()} a fost adaugat")
        except ValueError:
            print("Valoarea introdusa nu a fost intreaga")
        except RepoException as re:
            print(re)
        except ValidatorException as ve:
            print(ve)

    def __add_client_ui(self):
        """
        Adds a new client to the repository
        """
        try:
            id = int(input("Introduce un id: ").strip())
            name = input("Introduce un nume: ").strip()
            cnp = int(input("Introduce un cnp: ").strip())

            client = self.__client_service.add_client(id, name, cnp)

            print(f"Clientul cu id-ul {client.get_id()} a fost adaugat")
        except ValueError:
            print("Valoarea introdusa nu a fost intreaga")
        except RepoException as re:
            print(re)
        except ValidatorException as ve:
            print(ve)

    def __modify_film_ui(self):
        """
        Modifies a film from the repository
        """
        try:
            id = int(input("Introduce un id: ").strip())
            title = input("Introduce un titlu: ").strip()
            description = input("Introduce o descriere: ").strip()
            genre = input("Introduce un gen: ").strip()

            film = self.__film_service.modify_film(id, title, description, genre)

            print(f"Filmul cu id-ul {film.get_id()} a fost modificat")
        except ValueError:
            print("Valoarea introdusa nu a fost intreaga")
        except RepoException as re:
            print(re)
        except ValidatorException as ve:
            print(ve)

    def __modify_client_ui(self):
        """
        Modifies a film from the repository
        """
        try:
            id = int(input("Introduce un id: ").strip())
            name = input("Introduce un nume: ").strip()
            cnp = int(input("Introduce un cnp: ").strip())

            client = self.__client_service.modify_client(id, name, cnp)

            print(f"Clientul cu id-ul {client.get_id()} a fost modificat")
        except ValueError:
            print("Valoarea introdusa nu a fost intreaga")
        except RepoException as re:
            print(re)
        except ValidatorException as ve:
            print(ve)

    def __delete_film_ui(self):
        """
        Deletes a film from the repository
        """
        try:
            id = int(input("Introduce un id: ").strip())

            self.__film_service.delete_film(id)

            print(f"Filmul cu id-ul {id} a fost sters")
        except ValueError:
            print("Valoarea introdusa nu a fost intreaga")
        except RepoException as re:
            print(re)

    def __delete_client_ui(self):
        """
        Deletes a client from the repository
        """
        try:
            id = int(input("Introduce un id: ").strip())

            self.__client_service.delete_client(id)

            print(f"Clientul cu id-ul {id} a fost sters")
        except ValueError:
            print("Valoarea introdusa nu a fost intreaga")
        except RepoException as re:
            print(re)

    def __print_films_ui(self):
        """
        Prints all the films in the repository
        """
        films = self.__film_service.get_all_films()

        if not films:
            print("Nu exista filme in lista de filme")
            return

        print("Lista de filme adaugate contine:")

        for film in films:
            print(film)

    def __print_clients_ui(self):
        """
        Prints all the clients in the repository
        """
        clients = self.__client_service.get_all_clients()

        if not clients:
            print("Nu exista clienti in lista de clienti")
            return

        print("Lista de clienti adaugati contine:")

        for client in clients:
            print(client)

    def __find_client_by_cnp_ui(self):
        """
        Searches for the client with the given cnp in the repository and prints it if found
        """
        try:
            cnp = int(input("Introduceti un cnp: ").strip())

            client = self.__client_service.find_client_by_cnp(cnp)

            print(client)

        except ValueError:
            print("Valoarea introdusa nu a fost intreaga")
        except RepoException as re:
            print(re)

    def __filter_film_with_prefix_ui(self):
        """
        Filters the list of films using a given prefix
        """
        prefix = input("Introduceti un prefix pentru titlu: ").strip()

        films = self.__film_service.filter_film_with_prefix(prefix)

        if not films:
            print("Nu exista filme in lista de filme filtrata")
            return

        print("Lista de filme filtrate contine: ")

        for film in films:
            print(film)

    def __report_clients_by_name_ui(self):
        """
        Prints the report of clients with a list of films for each client, ordered by the name
        """
        report = self.__transaction_service.report_clients_by_name()

        if not report:
            print("Nu exista inchirieri")
            return

        for item in report:
            print(item)

    def __report_clients_by_number_ui(self):
        """
        Prints the report of clients with a lits of films for each client, ordered descending by the number of films rented
        """
        report = self.__transaction_service.report_clients_by_number()

        if not report:
            print("Nu exista inchirieri")
            return

        for item in report:
            print(item)

    def __report_films_ui(self):
        """
        Prints the report of films ordered descending by number of transactions for the film
        """
        report = self.__transaction_service.report_films()

        if not report:
            print("Nu exista inchirieri")
            return

        for item in report:
            print(item)

    def __report_first_clients_ui(self):
        """
        Prints the report of first 30% of clients order descending by the number of films rented
        """
        report = self.__transaction_service.report_first_clients()

        if not report:
            print("Nu exista inchirieri")
            return

        for item in report:
            print(item)

    def __report_last_films(self):
        """
        Prints the report of last(by the number of transactions) 50% films that start with a prefix ordered by title
        """
        prefix = input("Introduceti un prefix: ").strip()

        report = self.__transaction_service.report_last_films(prefix)

        if not report:
            print("Nu exista inchirieri")
            return

        for item in report:
            print(item)

    def __find_client_by_name_ui(self):
        """
        Searches for the clients with the given name in the repository and prints them if found any
        """
        name = input("Introduceti un nume: ").strip()

        clients = self.__client_service.find_client_by_name(name)

        if not clients:
            print("Nu au fost gasit niciun client")
            return

        for client in clients:
            print(client)

    def __find_film_by_title_ui(self):
        """
        Searches for the films with the given title in the repository and prints them if found any
        """
        title = input("Introduceti un titlu: ").strip()

        films = self.__film_service.find_film_by_title(title)

        if not films:
            print("Nu au fost gasit niciun film")
            return

        for film in films:
            print(film)

    def __rent_ui(self):
        """
        Rents a film to a client
        """
        try:
            id_transaction = int(input("Introduce un id pentru inchiriere: ").strip())
            id_film = int(input("Introduce id-ul filmului: ").strip())
            id_client = int(input("Introduce id-ul clientului: ").strip())

            self.__transaction_service.rent_film_to_client(id_transaction, id_film, id_client)

            print(f"Filmul cu id-ul {id_film} a fost inchiriat la clientul cu id-ul {id_client}")

        except ValueError:
            print("Valoarea introdusa nu a fost intreaga")
        except RepoException as re:
            print(re)
        except ValidatorException as ve:
            print(ve)

    def __return_ui(self):
        """
        Returns a film from a client
        """
        try:
            id_film = int(input("Introduce id-ul filmului: ").strip())
            id_client = int(input("Introduce id-ul clientului: ").strip())

            self.__transaction_service.return_film_from_client(id_film, id_client)

            print(f"Filmul cu id-ul {id_film} a fost returnat de catre clientul cu id-ul {id_client}")

        except ValueError:
            print("Valoarea introdusa nu a fost intreaga")
        except RepoException as re:
            print(re)

    def __random_ui(self):
        """
        Generates X random entities for each entity class (Film, Client, Transactions)
        """
        try:
            x = int(input("Introduce X-ul: ").strip())

            self.__film_service.generate_films_random(x)
            self.__client_service.generate_clients_random(x)
            self.__transaction_service.generate_transactions_random(x, tweak=True)  # more diverse generations

            print("Entitatile au fost generate cu succes")

        except ValueError:
            print("Valoare introdusa nu a fost intreaga")

    def __help_ui(self):
        """
        Prints a help menu
        """
        menu = """
        Meniu de help:
        
        add_film - adauga un film nou
        add_client - adauga un client nou
        modify_film - modifica un film existent
        modify_client - modifica un client existent
        delete_film - sterge un film existent
        delete_client - sterge un client existent
        print_films - afiseaza toate filmele adaugate
        print_clients - afiseaza toti clientii adaugati
        find_client_by_cnp - cauta un client dupa CNP
        find_client_by_name - cauta client dupa nume
        find_film_by_title - cauta film dupa titlu
        filter_film_with_prefix - filtreaza toate filmele cu conditia ca titlurile incep cu un prefix
        report_clients_by_name - generare raport clienti cu filme inchiriate ordonat dupa nume
        report_clients_by_number - generare raport clienti cu filme inchiriate ordonat dupa numarul de filme inchiriate
        report_films - generare raport cele mai inchiriate filme
        report_first_clients - generare raport primii 30% clienti cu cele mai multe filme 
        report_last_films - generare raport top 50% cele mai putin inchiriate filme care incep cu un string dat, sortate alfabetic dupa nume.
        rent - inchiriaza film catre client
        return - returneaza film de la client
        random - genereaza X entitati random pentru Film, Client, Inchiriere
        help - afiseaza acest meniu
        quit - paraseste aplicatia
        """

        print(menu)

    def start(self):
        """
        Starts the application
        """
        print("Bun venit la Inchiriere Filme v5.0\nFoloseste comanda help pentru mai multe detalii")

        while True:
            cmd = self.__get_command()

            options = self.__get_all_commands()
            if cmd in options:
                action = options[cmd]
                try:
                    action()  # invoke the selected action
                except IOError:
                    print("Eroare la nivel de fisiere")
            else:
                print("Comanda invalida")
