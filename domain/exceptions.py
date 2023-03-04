"""
Contains custom exceptions for the project
"""


class ValidatorException(Exception):
    """
    This exception is used to indicate a validation error
    """
    pass


class RepoException(Exception):
    """
    This exception is used to indicate a repository error
    """
    pass
