from datetime import datetime

from src.birthday import Birthday
from src.name import Name
from src.phone import Phone
from src.address import Address
from src.email import Email


class Record:
    """
    A class for storing contact information.

    Args:
        name (str): The name of the contact.

    Attributes:
        name (Name): The name of the contact.
        phones (list): A list of phone numbers for the contact.
        birthday (datetime.date): The birthday of the contact.

    """

    def __init__(self, name):
        self.name = name
        self.phones = []
        self.birthday = None
        self.address = None
        self.email = None

    def add_phone(self, phone):
        """
        Add a phone number to the contact.

        Args:
            phone (str): The phone number to add.

        Raises:
            ValueError: If the phone number is not a valid phone number.

        """
        new_phone = Phone(phone)
        new_phone.validate()
        self.phones.append(new_phone)

    def remove_phone(self, phone):
        """
        Remove a phone number from the contact.

        Args:
            phone (str): The phone number to remove.

        """
        self.phones = [p for p in self.phones if p.value != phone]

    def edit_phone(self, old_phone, new_phone):
        """
        Edit a phone number in the contact.

        Args:
            old_phone (str): The old phone number.
            new_phone (str): The new phone number.

        Raises:
            ValueError: If the new phone number is not a valid phone number.

        """
        self.remove_phone(old_phone)
        self.add_phone(new_phone)

    def find_phone(self, phone):
        """
        Find a phone number in the contact.

        Args:
            phone (str): The phone number to find.

        Returns:
            Phone: The phone number if found, else raises a ValueError.

        Raises:
            ValueError: If the phone number is not found.

        """
        for p in self.phones:
            if p.value == phone:
                return p
        raise ValueError("Phone not found.")

    def add_birthday(self, birthday):
        """
        Add a birthday to the contact.

        Args:
            birthday (str): The birthday in the format "dd.mm.yyyy".

        Raises:
            ValueError: If the birthday is not in the correct format.

        """
        self.birthday = Birthday(birthday)
        self.birthday.validate()
        self.birthday = datetime.strptime(birthday, "%d.%m.%Y")

    """Add method for adding address"""

    def add_address(self, address):
        """
        Add an address to the contact.

        """
        self.address = Address(address)

    def add_email(self, email):
        """
        Add an email to the contact.

        Args:
            email (str): The email to add.

        """
        self.email = Email(email)

    def get_birthday(self):
        """
        Get the birthday of the contact.

        Returns:
            str: The birthday in the format "dd.mm.yyyy".

        """
        return f"Contact name: {self.name.value} have birthday: {self.birthday.strftime('%d.%m.%Y')}"

    def __str__(self):
        """
        Return a string representation of the contact.

        Returns:
            str: The name and phone numbers of the contact.

        """
        return f"Contact name: {self.name.value} have phones: {'; '.join(p.value for p in self.phones)}"
