import sys
import os
import random
from cls.Round import Round
from cls.Person import Person
from cls.Drink import Drink 
from cls import FileManager
import table_maker

args = sys.argv
help = f"""HELP: brIW helps you collect drinks rounds. To start, just enter
    python3 {args[0]}
"""
if len(args) > 1:
    if args[1] == "-h":
        print(help)
    else:
        print("Argument not recognised. For help use -h.")
    exit()

menu = """
============== MENU ==============            {
                                           {   }
    [1] Get all people                      }_{ __{
    [2] Get all drinks                   .-{   }   }-.
    [3] Add people                      (   }     {   )
    [4] Add drinks                      |`-.._____..-'|
    [5] Get favourite drinks            |             ;--.
    [6] Set favourite drinks            |            (__  \\
    [E] Save & Exit                     |             | )  )
                                        |             |/  /
                                        |             /  / 
                                        |            (  /
                                        \             y'
                                         `-.._____..-'

"""
welcome = "Welcome to BrIW v0.1!"
people_file_path = "data/people.txt"
drinks_file_path = "data/drinks.txt"
preferences_file = "data/preferences.txt"
max_table_width = 90

def get_person_id(name):
    return people.index(name)+1

def get_drink_id(drink):
    return drinks.index(drink)+1

def get_person_from_id(name_id):
    return people[name_id-1]

def get_drink_from_id(drink_id):
    return drinks[drink_id-1]

def take_list_input(list_to_update, update_preferences=False):
    updated = False
    while True:
        item = input().strip().capitalize()
        if item == "":
            break

        if len(item) > max_table_width-6:
            print(f"Item not added - cannot be more than {max_table_width-6} characters. Try again.")
        else: 
            if update_preferences:
                try:
                    list_to_update.add_person(Person(item, Drink("")))
                except Exception as e:
                    print(str(e))
                    print("\nHit ENTER to return to menu")
                    break
            else: 
                list_to_update.add_drink(Drink(item))
            updated = True
            os.system("clear")
            print(f"{item} successfully added. Enter another or hit ENTER to return to menu.")
    os.system("clear")
    return list_to_update, updated

people_file = FileManager.PeopleFileManager(people_file_path)
people = people_file.get_people_from_file()

drinks_file = FileManager.DrinksFileManager(drinks_file_path)
drinks = drinks_file.get_drinks_from_file()

updated_people, updated_drinks, updated_preferences = False, False, False

os.system("clear")
print(welcome)

while True:
    print(menu)
    command = input("Enter a number to select a command: ")
    os.system("clear")
    if len(command) == 0:
        print("Expected input, none provided. ")
        input("Hit ENTER to return to menu.")

    elif command == "1":
        print(table_maker.print_single_column_table("People", people.get_names()))
        input("Hit ENTER to return to menu.")

    elif command == "2":
        print(table_maker.print_single_column_table("Drinks", drinks.get_names()))
        input("Hit ENTER to return to menu.")

    elif command == "3":
        print("Please enter a name to add. Hit enter when done to add another. ")
        people, success = take_list_input(people, True)
        if success:
            updated_people = True

    elif command == "4":
        print("Please enter a drink to add: ")
        drinks, success = take_list_input(drinks)
        if success:
            updated_drinks = True

    elif command == "5":
        print(table_maker.print_people_drinks(people))
        input("Hit ENTER to return to menu.")

    elif command == "6":
        print(table_maker.print_single_column_table("People", people.get_names()))
        print("To set a favourite drink, enter the name of a person.")
        name = input("Enter a name: ").capitalize()
        if name == "":
            continue
        elif not people.check_person_exists(name):
            print(f"Person {name} not recognised.")
            input("Hit ENTER to return to menu: ")
            os.system("clear")
            continue
        person = people.get_person(name)

        print(table_maker.print_single_column_table("Drinks", drinks.get_names()))
        print("Now enter the name of their favourite drink.")
        drink_name = input("Enter a drink name: ").capitalize()
        if drink_name == "":
            continue
        elif not drinks.check_drink_exists(drink_name):
            print(f"Drink {drink_name} not recognised.")
            input("Hit ENTER to return to menu: ")
            os.system("clear")
            continue
        drink = drinks.get_drink(drink_name)
        
        person.favourite_drink = drink
        people.update_person(person)
        updated_people, updated_drinks = True, True
        os.system("clear")
        print(f"{name}'s favourite drink is now {drink_name}.\n")
        input("Hit ENTER to return to menu.")

    elif command.lower() == "e":
        break

    else: 
        print("Unrecognised command. ")
    os.system("clear")

if updated_people:
    people_file.update_file(people)
    # update_list_file(people_file, people)
if updated_drinks:
    drinks_file.update_file(drinks)
    # update_list_file(drinks_file, drinks)