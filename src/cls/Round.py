from src import table_maker
from src.cls.Person import *
from src.cls.Drink import *
from prettytable import PrettyTable

class Round:

    def __init__(self, owner, time_started, active=False):
        self.owner = owner.name
        self.orders = {}
        self.time_started = time_started
        self.active = active

    def __str__(self):
        round_text = f"Round started by {self.owner} at {self.time_started}: \n\n"
        round_table = PrettyTable(["Person", "Drink"])
        for name, drink in self.orders.items():
            round_table.add_row([name, drink])
        round_text += round_table.get_string() + "\n\n"
        return round_text

    def get_peoples_names(self):
        return orders.keys()

    def get_drinks_names(self):
        return orders.values()

    def add_order(self, person, drink):
        if not isinstance(person, Person):
            raise TypeError(f"Round.add_order(): Expected a Person object, received a {type(person)} object instead.")
        elif not isinstance(drink, Drink):
            raise TypeError(f"Round.add_order(): Expected a Drink object, received a {type(drink)} object instead.")
        self.orders[person.name] = drink.name

    def make_csv_line(self):
        line = f"{self.active},{self.owner},"
        for person, drink in self.orders.items():
            line += f"{person.name}:{drink.name},"
        return line

    def print_orders(self):
        return table_maker.print_people_drinks(orders, ("Name", "Drink"))

class Rounds:

    def __init__(self, rounds=[]):
        self.all_rounds = []
        self.add_rounds(rounds)

    def add_round(self, round):
        if not isinstance(round, Round):
            raise TypeError(f"Round.add_round(): Expected a Round object, received a {type(round)} object instead.")
        self.all_rounds.append(round)

    def add_rounds(self, rounds):
        for round in rounds:
            self.add_round(round)

    def get_active_rounds(self):
        active_rounds = []
        for round in self.all_rounds:
            if round.active:
                active_rounds.append(round)
        return active_rounds