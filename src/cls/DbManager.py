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
        print("Setting database connection")
        connection = pymysql.connect(
            hostname,
            username,
            password,
            database_name,
            autocommit=True
        )
        with connection.cursor() as db:
            print("About to execute query...")
            db.execute(query, param)
            print("Executed query")
            try:
                db.lastrowid
            except Exception as e:
                print(e)
            return db.lastrowid
    
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
        rounds = []
        try: 
            results = DbManager.execute_select("SELECT active, time_started, person_name as owner_name FROM rounds JOIN people on person_id=owner_id;")
            for row in results:
                print(row)
                round = make_a_round_from_string_values(row[0], row[1], row[2])
                rounds.append(round)
        except Exception as e:
            print(e)
        return rounds

    # def get_round(self):


    def update_round(updated_round):
        query = f"UPDATE rounds SET active={updated_round.active}"
        return DbManager.execute_update_or_insert(query)


    def add_round(new_round):
        query = f"INSERT INTO rounds (active, time_started, owner_id) VALUES (%s, %s, (SELECT person_id FROM people WHERE person_name=%s))"
        param = (new_round.get_active_as_int(), new_round.time_started, new_round.owner)
        
        round_id = DbManager.execute_update_or_insert(query, param)
        print(f"Inserted round {round_id}")

        # for person, drink in new_round.orders.items():
        #     RoundsDbManager.add_order_to_round(round_id, (person, drink))

        return round_id

    # def add_order_to_round(round_id, order):
    #     print(f"order: {order}")
    #     query=f"INSERT INTO orders (person_id, drink_id, round_id) VALUES ((SELECT person_id FROM people WHERE person_name=%s), (SELECT drink_id FROM drinks WHERE drink_name=%s), %s)"
    #     param=(order[0], order[1], round_id)
    #     DbManager.execute_update_or_insert(query, param)
