from src.field import Field


class Adress(Field):
    """
    A class that represents an adress.

    Parameters:
        value (str): The adresses value.

    Attributes:
        value (str): The adresses value.
    """

    def __init__(self, value):
        """
        Initializes a new instance of the Adress class.

        Parameters:
        value (str): The adresses value.
        """
        super().__init__(value)
