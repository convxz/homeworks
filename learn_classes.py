class House:
    """Описание дома"""
    def __init__(self, street, number):
        self.street = street
        self.number = number
        self.age = 0

    def build(self):
        """строит дом"""
        print(f"Дом на улице {self.street} под номером {self.number} построен.")

    def age_of_house(self, year):
        """Возраст дома"""
        self.age += year


class ProspectHouse(House):
    """пример наследования"""
    def __init__(self, prospect, number):
        super().__init__(self, number)
        self.Prospect = prospect


Pr_house = ProspectHouse("Мира", 23)
print(Pr_house.Prospect)
