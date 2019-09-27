import src.helper
from src.cls.Person import Person, People
from src.cls.Drink import Drink, Drinks
from src.cls.Round import *
from src.cls.param import *
import pymysql
from datetime import datetime

class DbManager:
    datetime_format = "%d.%m.%y %H:%M:%S"

    # def query_builder(self, columns, table, where_conditions="", orderby=""):
    #     query = f"SELECT {columns} FROM {table}"
    #     if where_conditions != "":
    #         query += " "

    def execute_select(query, param=tuple()):
        connection = pymysql.connect(
            hostname,
            username,
            password,
            database_name,
            autocommit=True
        ) 
        with connection.cursor() as db:
        # Want another try?
            db.execute(query, param)
            results = db.fetchall()
        return results

    def execute_update_or_insert(query, param=tuple()):
        connection = pymysql.connect(
            hostname,
            username,
            password,
            database_name,
            autocommit=True
        )
        with connection.cursor() as db:
            db.execute(query, param)
            return db.affected_rows()
    
class PeopleDbManager(DbManager):
        
    def get_all_people(self, drinks):
        people = People()
        try:
            results = DbManager.execute_select("SELECT person_name, drink_name FROM people LEFT JOIN drinks ON people.favourite_drink_id=drinks.drink_id")
        except Exception as e:
            # TODO: improve this sad message
            print("Something went wrong...")
            print(e)
        for row in results:
            print(row)
            people.add_person(Person(row[0], drinks.get_drink(row[1])))

        return people

    # def update_file(self, updated_people):
    #     rows = []
    #     for person in updated_people.all_people.values():
    #         rows.append(person.make_csv_line())
    #     FileManager.overwrite_file(self, rows)

class DrinksDbManager(DbManager):

    def get_all_drinks(self):
        drinks = Drinks()
        try:
            results = DbManager.execute_select("SELECT drink_name FROM drinks")
            for row in results:
                print(row)
                drinks.add_drink(Drink(row[0]))
        except Exception as e:
            # TODO: improve this sad message
            print("Something went wrong...")
            print(e)

        return drinks

    # def update_file(updated_drinks):
    #     rows = []
    #     for drink in updated_drinks.all_drinks.values():
    #         rows.append(drink.make_csv_line())
    #     FileManager.overwrite_file(self, rows)

class RoundsDbManager:

    def get_all_rounds(self):
        rounds = Rounds()
        try: 
            results = DbManager.execute_select("SELECT active, time_started, person_name as owner_name FROM rounds JOIN people on person_id=owner_id;")
            for row in results:
                print(row)
                string_data = make_a_round_from_string_values(row[0], row[1], row[2])
                rounds.add_round(string_data)
        except:
            # cry
            pass

    def update_round(self, updated_round):
        query = f"UPDATE rounds SET active={updated_round.active}"
        return DbManager.execute_update_or_insert(query)


    def add_round(self, new_round):
        query = "INSERT INTO rounds ("
        + "active, time_started, owner_id"
        + ") VALUES ("
        + f"{new_round.active}, "
        + f"{new_round.time_started}, "
        + f"SELECT person_id FROM people WHERE person_name={new_round.owner}))"
        success =  (DbManager.execute_update_or_insert(query) == 1)

        # for order in new_round.orders

    def add_order_to_round(self, round_id, order):
        pass
