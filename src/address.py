from src.field import Field


class Address(Field):
    """
    A class that represents an address.

    Parameters:
        value (str): The address value.

    Attributes:
        value (str): The address value.
    """

    def __init__(self, value):
        """
        Initializes a new instance of the Address class.

        Parameters:
        value (str): The address value.
        """
        super().__init__(value)
