"""
Class definitions of the validators for the entities in the project
"""
from domain.exceptions import ValidatorException


class FilmValidator:
    """
    Validator for a Film instance
    """

    def validate(self, film):
        """
        Validates the film,
        checks if the id is not negative and the title, description and genre are not empty strings

        :param film: Film object
        :raises ValidatorException: if the film object contains invalid values
        """
        errors = ""
        if film.get_id() <= 0:
            errors += "Id invalid\n"
        if film.get_title() == "":
            errors += "Titlu invalid\n"
        if film.get_description() == "":
            errors += "Descriere invalida\n"
        if film.get_genre() == "":
            errors += "Gen invalid\n"

        if errors != "":
            raise ValidatorException(errors)


class ClientValidator:
    """
    Validator for a Client instance
    """
    def validate(self, client):
        """
        Validates the client,
        checks if the id is not negative, the name is not an empty string and the CNP is valid (remark: simplified)

        :param client: Client object
        :raises ValidatorException: if the client contains invalid values
        """
        errors = ""
        if client.get_id() <= 0:
            errors += "Id invalid\n"
        if client.get_name() == "":
            errors += "Nume invalid\n"
        if len(str(client.get_cnp())) != 13:  # the CNP must have 13 digits
            errors += "CNP invalid\n"

        if errors != "":
            raise ValidatorException(errors)


class TransactionValidator:
    """
    Validator for a Transaction instance
    """
    def validate(self, transaction):
        """
        Validated the transaction,
        checks if the id is not negative

        :param transaction: Transaction object
        :raises ValidatorException: if the transaction contains invalid values
        """
        if transaction.get_id() <= 0:
            raise ValidatorException("Id invalid\n")
