from collections import UserDict, defaultdict
from datetime import datetime
from src.record import Record


class AddressBook(UserDict):
    def add_record(self, record: Record):
        if record.name.value in self.data:
            raise ValueError(f"Contact {record.name.value} already exists.")
        self.data[record.name.value] = record

    def find(self, name):
        if name in self.data:
            return self.data[name]
        raise ValueError(f"Contact {name} not found.")

    def delete(self, name):
        if name not in self.data:
            raise ValueError(f"Contact {name} not found.")
        del self.data[name]

    def get_birthdays_per_week(self):
        today = datetime.today().date()
        res = defaultdict(list)

        for name, record in self.data.items():
            if record.birthday:
                birthday = record.birthday.date()
                birthday_this_year = birthday.replace(year=today.year)
                if birthday_this_year < today:
                    birthday_this_year = birthday_this_year.replace(year=today.year + 1)
                delta_days = (birthday_this_year - today).days
                if delta_days < 7:
                    birthday_week_day = birthday_this_year.strftime("%A")
                    if birthday_week_day == ("Sunday" or "Saturday"):
                        res["Monday"].append(record.name.value)
                    else:
                        res[birthday_week_day].append(record.name.value)

        for key, value in res.items():
            birth_name = ", ".join(value)
            print(f"{key}: {birth_name}")
