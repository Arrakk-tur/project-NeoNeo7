class Field:
    """
    A class that represents a field in an application.

    Parameters:
    value (any): The value of the field.

    Attributes:
    value (any): The value of the field.
    """

    def __init__(self, value):
        """
        Initializes a new instance of the Field class.

        Parameters:
        value (any): The value of the field.
        """
        self.value = value

    def __str__(self):
        """
        Returns a string representation of the field.

        Returns:
        str: A string representation of the field.
        """
        return str(self.value)
