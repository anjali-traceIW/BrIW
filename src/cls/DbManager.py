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

    def get_orders_for_a_round(self, round_id):
        orders = {}
        # Could this be shorter? I don't think this cold be shorter.
        query = "SELECT person_name, drink_name FROM drinks JOIN (SELECT person_name, drink_id FROM people JOIN (SELECT person_id, drink_id FROM orders WHERE round_id = %s) AS order_info ON people.person_id=order_info.person_id) AS person_drink_id ON drinks.drink_id=person_drink_id.drink_id"
        try:
            results = DbManager.execute_select(query, (round_id))
        except Exception as e:
            print(e)
        for row in results:
            orders[row[0]] = row[1]  # This is stupid
        return orders

    def get_all_rounds(self):
        rounds = []
        # try: 
        results = DbManager.execute_select("SELECT round_id, active, time_started, person_name FROM rounds JOIN people on person_id=owner_id;")
        for row in results:
            print(row)
            round = Round(owner=row[3], time_started=row[2], active=(row[1] == 1))
            # round = make_a_round_from_string_values(row[1], row[2], row[3])
            orders = self.get_orders_for_a_round(row[0])
            print(f"Orders: {orders}")
            round.orders = orders
            print(round)
            rounds.append(round)
        # except Exception as e:
        #     print(f"get_all_rounds: {e}")
        
        return rounds

    def get_round(self, round_id):
        query = "SELECT active, time_started, person_name FROM rounds JOIN people on person_id=owner_id WHERE round_id=%s;"
        try: 
            result = DbManager.execute_select(query, (round_id))[0] # Returns a tuple (single result)
        except Exception as e:
            print(e)

        return Round(result[2], result[1], result[0])

    def update_round(updated_round):
        query = f"UPDATE rounds SET active={updated_round.active}"
        try:
            return DbManager.execute_update_or_insert(query)
        except Exception as e:
            print(e)

    def add_round(new_round):
        query = f"INSERT INTO rounds (active, time_started, owner_id) VALUES (%s, CURRENT_TIMESTAMP, (SELECT person_id FROM people WHERE person_name=%s))"
        param = (new_round.get_active_as_int(), new_round.owner)
        
        round_id = DbManager.execute_update_or_insert(query, param)
        print(f"Inserted round {round_id}")

        for person, drink in new_round.orders.items():
            order_id = RoundsDbManager.add_order_to_round(round_id, (person, drink))
            
        return round_id

    def add_order_to_round(round_id, order):
        print(f"order: {order}")
        query=f"INSERT INTO orders (person_id, drink_id, round_id) VALUES ((SELECT person_id FROM people WHERE person_name=%s), (SELECT drink_id FROM drinks WHERE drink_name=%s), %s)"
        param=(order[0], order[1], round_id)
        return DbManager.execute_update_or_insert(query, param)
