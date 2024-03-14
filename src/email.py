from src.field import Field


class Email(Field):
    """
    A class that represents a email.

    Args:
        value (str): The Email value to be validated and formatted.

    """

    def __init__(self, value):
        super().__init__(value)
