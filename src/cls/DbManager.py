import src.helper
from src.cls.Person import Person, People
from src.cls.Drink import Drink, Drinks
from src.cls.Round import *
from src.cls.param import *
import pymysql
from datetime import datetime

class DbManager:
    datetime_format = "%d.%m.%y %H:%M:%S"

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
        
    def get_all_people():
        people = []
        try:
            results = DbManager.execute_select("SELECT person_name, drink_name FROM people LEFT JOIN drinks ON people.favourite_drink_id=drinks.drink_id")
            for row in results:
                # print(row)
                people.append(Person(row[0], Drink(row[1])))
        except Exception as e:
            # TODO: improve this sad message
            print("Something went wrong getting all people from the database...")
            print(e)
        return people

    def get_person(person_id):
        person = Person("")
        query = "SELECT person_name, drink_name FROM people JOIN drinks ON favourite_drink_id = drink_id WHERE person_id=%s"
        try: 
            results = DbManager.execute_select(query, (person_id))
            person = Person(results[0], Drink(results[1]))
        except Exception as e:
            print(e)
        return person

    def create_person(person):
        new_person_id = -1
        query = "INSERT INTO people (person_name, favourite_drink_id) VALUES (%s, (SELECT drink_id FROM drinks WHERE drink_name = %s))"
        try:
            new_person_id = DbManager.execute_update_or_insert(query, (person.name, person.favourite_drink.name))
        except Exception as e:
            print(e)
        return new_person_id


class DrinksDbManager(DbManager):

    def get_all_drinks():
        drinks = []
        try:
            results = DbManager.execute_select("SELECT drink_name FROM drinks")
            for row in results:
                print(row)
                drinks.append(Drink(row[0]))
        except Exception as e:
            # TODO: improve this sad message
            print("Something went wrong getting all drinks from the database...")
            print(e)
        return drinks

    def get_drink(drink_id):
        drink = Drink("")
        try: 
            result = DbManager.execute_select("SELECT drink_name FROM drinks WHERE drink_id=%s", (drink_id))[0]     # Only one result to be returned.
            drink = Drink(result[0])
        except Exception as e:
            print(e)
        return drink

    def create_drink(drink):
        new_drink_id = -1
        query = "INSERT INTO drinks (drink_name) VALUES (%s)"
        try: 
            new_drink_id = DbManager.execute_update_or_insert(query, (drink.name))
        except Exception as e:
            print(e)
        return new_drink_id


class RoundsDbManager(DbManager):

    def get_all_rounds():
        rounds = []
        try: 
            results = DbManager.execute_select("SELECT round_id, active, time_started, person_name FROM rounds JOIN people on person_id=owner_id;")
            for row in results:
                round = Round(owner=row[3], time_started=row[2], active=(row[1] == 1))
                orders = DbManager.get_orders_for_a_round(row[0])
                round.orders = orders
                rounds.append(round)
        except Exception as e:
            print(e)
        return rounds

    def get_round(round_id):
        round = Round("", "")
        query = "SELECT active, time_started, person_name FROM rounds JOIN people on person_id=owner_id WHERE round_id=%s;"
        try: 
            result = DbManager.execute_select(query, (round_id))[0] # Returns a tuple (single result)
            round = Round(result[2], result[1], result[0])
        except Exception as e:
            print(e)
        return round

    def create_round(new_round):
        round_id = -1
        query = f"INSERT INTO rounds (active, time_started, owner_id) VALUES (%s, CURRENT_TIMESTAMP, (SELECT person_id FROM people WHERE person_name=%s))"
        param = (new_round.get_active_as_int(), new_round.owner)
        try:
            round_id = DbManager.execute_update_or_insert(query, param)
            # print(f"Inserted round {round_id}")
            for person, drink in new_round.orders.items():
                order_id = RoundsDbManager.add_order_to_round(round_id, (person, drink))
        except Exception as e:
            print(e)
        return round_id

    def get_orders_for_round(round_id):
        orders = {}
        # Could this be shorter? I don't think this could be shorter.
        query = "SELECT person_name, drink_name FROM drinks JOIN (SELECT person_name, drink_id FROM people JOIN (SELECT person_id, drink_id FROM orders WHERE round_id = %s) AS order_info ON people.person_id=order_info.person_id) AS person_drink_id ON drinks.drink_id=person_drink_id.drink_id"
        try:
            results = DbManager.execute_select(query, (round_id))
        except Exception as e:
            print(e)
        for row in results:
            orders[row[0]] = row[1]  # This is stupid?
        return orders

    def create_order_for_round(round_id, order):
        new_order_id = -1
        # print(f"order: {order}")
        query="INSERT INTO orders (person_id, drink_id, round_id) VALUES ((SELECT person_id FROM people WHERE person_name=%s), (SELECT drink_id FROM drinks WHERE drink_name=%s), %s)"
        param=(order[0], order[1], round_id)
        try: 
            new_order_id = DbManager.execute_update_or_insert(query, param)
        except Exception as e:
            print(e)
        return new_order_id