import src.helper
from src.cls.Person import Person, People
from src.cls.Drink import Drink, Drinks
from src.cls.Round import Round, Rounds

class FileManager:

    def __init__(self, file_path):
        if file_path == "":
            raise ValueError("No file supplied.")
        self.file_path = file_path

    def read_file(self):
        items = []
        try:
            with open(self.file_path,"rt",newline="\n") as file:
                for line in file:
                    if line[:-1] != "":
                        items.append(line[:-1].capitalize())
        except FileNotFoundError:
            src.helper.ask_to_continue(f"Invalid file supplied: {self.file_path}")

        if len(items) == 0:
            src.helper.ask_to_continue(f"Empty file supplied: {self.file_path}")

        return items

    def overwrite_file(self, new_lines):
        with open(self.file_path,"w") as file:
            for line in new_lines:
                file.write(f"{line}\n")
    
class PeopleFileManager(FileManager):

    def get_people_from_file(self):
        people = People()
        rows = FileManager.read_file(self)
        for row in rows:
            new_row = [x.strip() for x in row.split(',')]
            people.add_person(Person(new_row[0], Drink(new_row[1])))
        return people

    def update_file(self, updated_people):
        rows = []
        for person in updated_people.all_people.values():
            rows.append(person.make_csv_line())
        FileManager.overwrite_file(self, rows)

class DrinksFileManager(FileManager):

    def get_drinks_from_file(self):
        drinks = Drinks()
        rows = FileManager.read_file(self)
        for row in rows:
            new_row = [x.strip() for x in row.split(',')]
            drinks.add_drink(Drink(new_row[0]))
        return drinks

    def update_file(self, updated_drinks):
        rows = []
        for drink in updated_drinks.all_drinks.values():
            rows.append(drink.make_csv_line())
        FileManager.overwrite_file(self, rows)

class RoundsFileManager(FileManager):

    def get_rounds_from_file(self, people, drinks):
        rounds = Rounds()
        rows = FileManager.read_file(self)
        for row in rows:
            new_row = [x.strip() for x in row.split(',')]
            round = Round(owner=new_row[1], active=new_row[0])
            for order in new_row[2:]:
                # Of the format 'name:drink_name'
                order = [x.strip() for x in order.split(':')]
                person = people.get_person(order[0])
                drink = drinks.get_drink(order[1])
                round.add_order(person,drink)
            rounds.add_round(round)
        return drinks

    def update_file(self, updated_rounds):
        rows = []
        for round in updated_rounds.all_rounds:
            rows.append(round.make_csv_line())
        FileManager.overwrite_file(self, rows)
        