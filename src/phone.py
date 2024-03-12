from src.field import Field


class Phone(Field):
    """
    A class that represents a phone numbers.

    Parameters:
        value (str): The phone number to be validated and formatted.

    """

    def __init__(self, value):
        super().__init__(value)

    def validate(self):
        """
        Validates that the phone number is a 10-digit number.

        Raises:
            ValueError: If the phone number is not a 10-digit number.

        """
        if len(self.value) != 10 or not self.value.isdigit():
            raise ValueError("Phone number should contained 10 digits")
