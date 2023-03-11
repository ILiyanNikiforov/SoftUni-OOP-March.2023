class DVD:

    def __init__(self, name: str, id_num: int, creation_year: int, creation_month: str, age_restriction: int):
        self.name = name
        self.id = id_num
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    @classmethod
    def from_date(cls, id: int, name: str, date: str, age_restriction: int):
        splitted_date = date.split(".")
        month = int(splitted_date[1])
        year = int(splitted_date[2])
        return cls(name, id, year, months_num_to_str[month], age_restriction)

    def __repr__(self):
        if self.is_rented:
            status = 'rented'
        else:
            status = 'not rented'
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) has age restriction" \
               f" {self.age_restriction}. Status: {status}"


months_num_to_str = {
     1: "January",
     2: "February",
     3: "March",
     4: "April",
     5: "May",
     6: "June",
     7: "July",
     8: "August",
     9: "September",
     10: "October",
     11: "November",
     12: "December"
}
