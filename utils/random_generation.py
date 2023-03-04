"""
Utility functions for random generation of objects
"""
import random
import string


def generate_random_string(length):
    """
    Generates a random string of characters (letters and digits) with the size length
    :param length: integer
    :return: the generated string
    """
    alphabet = string.ascii_letters + string.digits
    result = "".join(random.choice(alphabet) for _ in range(length))

    return result


def generate_random_cnp():
    """
    Generates a random CNP in a simplified manner
    :return: the generated integer representing the CNP
    """
    alphabet = "123456789"
    result = random.choice(alphabet)
    result += "".join(random.choice(string.digits) for _ in range(12))

    return result
