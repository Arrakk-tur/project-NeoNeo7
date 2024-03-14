from src.field import Field


class Name(Field):
    """
    A class that represents a name.

    Parameters:
        value (str): The name's value.

    Attributes:
        value (str): The name's value.
    """

    def __init__(self, value):
        """
        Initializes a new instance of the Name class.

        Parameters:
        value (str): The name's value.
        """
        super().__init__(value)
