from src import table_maker
from src.cls.Person import *
from src.cls.Drink import *
from prettytable import PrettyTable
from datetime import datetime

class Round:

    def __init__(self, owner, time_started, active=False):
        if isinstance(owner, Person):
            self.owner = owner.name
        elif isinstance(owner, str):
            self.owner = owner
        else:
            raise TypeError(f"Expected Person object or string person name to create a round. Recieved {type(owner)}")
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

    def get_active_as_int(self):
        if self.active:
            return 1
        return 0

    def add_order(self, person, drink):
        if not isinstance(person, Person):
            raise TypeError(f"Round.add_order(): Expected a Person object, received a {type(person)} object instead.")
        elif not isinstance(drink, Drink):
            raise TypeError(f"Round.add_order(): Expected a Drink object, received a {type(drink)} object instead.")
        self.orders[person.name] = drink.name

    def make_csv_line(self, datetime_format):
        line = f"{self.time_started.strftime(datetime_format)},{self.active},{self.owner.capitalize()},"
        for person, drink in self.orders.items():
            line += f"{person.name}:{drink.name},"
        return line[:-1]

    def print_orders(self):
        return table_maker.print_people_drinks(orders, ("Name", "Drink"))

    def make_json_obj(self):
        return { 'time_started':str(self.time_started), 'active':self.active, 'owner':self.owner , 'orders':self.orders}

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

    def make_json_obj(self):
        rounds_list = []
        for round in self.all_rounds:
            rounds_list.append(round.make_json_obj())
        return {"all_rounds": rounds_list}

def encode_a_round(self, round):
    return {'time_started':round.time_started, 'active': round.active, 'owner':round.owner , 'orders':round.orders}

def make_a_round_from_string_values(active, time_started, owner, orders="\{\}"):
    string_data = {}
    string_data["active"] = active
    string_data["time_started"] = time_started
    string_data["owner"] = owner
    string_data["orders"] = orders
    return decode_a_round(string_data)

def decode_a_round(data):
    owner = data["owner"]
    time_started = data["time_started"]
    active = (data["active"] == "True")
    orders = data["orders"]#.__dict__

    round = Round(owner, time_started, active)
    round.orders = orders

    return round
    