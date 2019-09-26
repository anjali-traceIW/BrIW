import src.helper
from src.cls.Person import Person, People
from src.cls.Drink import Drink, Drinks
from src.cls.Round import Round, Rounds
from src.cls.param import *
import pymysql
from datetime import datetime

class FileManager:
    datetime_format = "%d.%m.%y %H:%M:%S"

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
            src.helper.ask_a_question_to_continue(f"Invalid file supplied: {self.file_path}")
            return items

        if len(items) == 0:
            src.helper.ask_a_question_to_continue(f"Empty file supplied: {self.file_path}")

        return items

    def execute_query(self, query, param=tuple()):
        with pymysql.connect(
            hostname,
            username,
            password,
            database_name,
            autocommit=True
        ) as db:
        # Want another try?
            db.execute(query)
            results = db.fetchall()
        return results

    def overwrite_file(self, new_lines):
        with open(self.file_path,"w") as file:
            for line in new_lines:
                file.write(f"{line}\n")
    
class PeopleFileManager(FileManager):
        
    def get_people_from_db(self, drinks):
        people = People()
        try:
            results = FileManager.execute_query(self, "SELECT person_name, drink_name FROM people LEFT JOIN drinks ON people.favourite_drink_id=drinks.drink_id")
        except Exception as e:
            # TODO: improve this sad message
            print("Something went wrong...")
            print(e)
        for row in results:
            print(row)
            people.add_person(Person(row[0], drinks.get_drink(row[1])))

        return people

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

    def get_drinks_from_db(self):
        drinks = Drinks()
        try:
            results = FileManager.execute_query(self, "SELECT drink_name FROM drinks")
            for row in results:
                print(row)
                drinks.add_drink(Drink(row[0]))
        except Exception as e:
            # TODO: improve this sad message
            print("Something went wrong...")
            print(e)

        return drinks

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
            new_row = [x.strip().capitalize() for x in row.split(',')]
            time_started = datetime.strptime(new_row[0], FileManager.datetime_format)
            owner = people.get_person(new_row[2])
            active = (new_row[1] == "True") # Make a boolean value
            round = Round(owner, time_started, active)
            for order in new_row[3:]:
                # Of the format 'person_name:drink_name'
                order = [x.strip().capitalize() for x in order.split(':')]
                print(order)
                print(drinks.all_drinks)
                person = people.get_person(order[0])
                drink = drinks.get_drink(order[1])
                round.add_order(person, drink)
            rounds.add_round(round)
        return rounds

    def update_file(self, updated_rounds):
        rows = []
        for round in updated_rounds.all_rounds:
            rows.append(round.make_csv_line(FileManager.datetime_format))
        FileManager.overwrite_file(self, rows)
