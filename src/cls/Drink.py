class Drink:

    def __init__(self, name, temp=""):
        if name is not None:    # Can have an empty drink (e.g. when making a person with no favourite drink)
            self.name = name.strip().capitalize()
        else:
            self.name = ""
        self.temperature = temp

    def __eq__(self, other_drink):
        return self.name == other_drink.name and self.temperature == other_drink.temperature

    def make_csv_line(self):
        return f"{self.name},{self.temperature}"

    def to_json(self):
        # json_str = '{ "name":"John", "age":30, "city":"New York"}'
        return { "drink_name": self.name, "temperature": self.temperature }

class Drinks:

    def __init__(self, drinks=[]):
        self.all_drinks = {}
        self.add_drinks(drinks)

    def __eq__(self, other_drinks):
        if len(self.all_drinks.keys()) != len(other_drinks.all_drinks.keys()):
            return False
        for drink_name in self.all_drinks.keys():
            try: 
                if not self.get_drink(drink_name) == other_drinks.get_drink(drink_name):
                    # Both contain the drink with name drink_name, but different versions of it
                    return False
            except:
                # other_drinks does not contain one of the drinks
                return False
        return True

    def add_drink(self, drink):
        if drink.name in self.all_drinks.keys():
            raise Exception(f"Drink {drink.name} already exists.")
        self.all_drinks[drink.name] = drink

    def add_drinks(self, drinks):
        for drink in drinks:
            self.add_drink(drink)

    def get_drink(self, drink_name):
        return self.all_drinks[drink_name]

    def get_names(self):
        return list(self.all_drinks.keys())

    def check_drink_exists(self, drink_name):
        return drink_name in self.all_drinks.keys()

    def make_json_str(self):
        # json_str = '{ "name":"John", "age":30, "city":"New York"}'
        json_str = "{ 'all_drinks': {"
        for drink in self.all_drinks.values():
            json_str += f" '{drink.name}':'{drink.make_json_str()}',"
        json_str = json_str[:-1] + "}}"   # Remove final comma
        return json_str
        