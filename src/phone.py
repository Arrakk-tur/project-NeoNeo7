import re

from src.field import Field


class Phone(Field):
    """
    A class that represents a phone numbers.

    Parameters:
        value (str): The phone number to be validated and formatted.

    """

    def __init__(self, value):
        if not re.fullmatch(r"\d{10}", value):
            raise ValueError("Phone number must contain 10 digits")
        super().__init__(value)
