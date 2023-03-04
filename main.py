"""
Scrieți o aplicație pentru o firmă de închiriere de filme.
"""
from repositories.client_file_repository import ClientFileRepository
from repositories.client_repository import ClientRepository
from repositories.film_file_repository import FilmFileRepository
from repositories.transaction_file_repository import TransactionFileRepository
from repositories.transaction_repository import TransactionRepository
from services.film_service import FilmService
from services.client_service import ClientService
from services.transaction_service import TransactionService
from domain.validators import FilmValidator, ClientValidator, TransactionValidator
from repositories.film_repository import FilmRepository
from ui.console import Console


def run():
    """
    Initializes the application
    """
    # film_repo = FilmRepository()
    film_repo = FilmFileRepository("films.txt")
    film_valid = FilmValidator()
    film_srv = FilmService(film_repo, film_valid)

    # client_repo = ClientRepository()
    client_repo = ClientFileRepository("clients.txt")
    client_valid = ClientValidator()
    client_srv = ClientService(client_repo, client_valid)

    # transaction_repo = TransactionRepository()
    transaction_repo = TransactionFileRepository("transactions.txt", film_repo, client_repo)
    transaction_valid = TransactionValidator()
    transaction_srv = TransactionService(transaction_repo, transaction_valid, film_repo, client_repo)

    ui = Console(film_srv, client_srv, transaction_srv)
    ui.start()


run()
