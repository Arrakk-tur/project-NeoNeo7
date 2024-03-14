import re

from src.field import Field


class Birthday(Field):
    """
    A class that represents a birthdays.

    Args:
        value (str): The birthday value to be validated and formatted.

    """

    def __init__(self, value):
        super().__init__(value)

    def validate(self):
        """
        Validate the birthday value.

        Raises:
            ValueError: If the value is not a valid birthday.

        """
        if (
            re.match(
                "^(3[01]|[12][0-9]|0?[1-9])\.(0[1-9]|1[1,2])\.(19|20)\d{2}", self.value
            )
            is None
        ):
            raise ValueError("Invalid date format. Must be 'DD.MM.YYYY'")
