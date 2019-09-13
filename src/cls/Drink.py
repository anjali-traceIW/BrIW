class Drink:

    def __init__(self, name, temp=""):
        self.name = name
        self.temperature = temp

class Drinks:

    def __init__(self, drinks=[]):
        self.all_drinks = {}
        self.add_drinks(drinks)

    def add_drink(self, drink):
        if drink.name in self.all_drinks.keys():
            raise Exception(f"Drink {drink.name} already exists.")
        self.all_drinks[drink.name] = drink

    def add_drinks(self, drinks):
        for drink in drinks:
            self.add_drink(drink)