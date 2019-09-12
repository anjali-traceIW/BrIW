import sys
import os
import random
from cls import Round, Person, Drink, FileManager
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
people_file = "data/people.txt"
drinks_file = "data/drinks.txt"
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

def set_preference(name_id, drink_id):
    preferences[name_id] = drink_id

def take_list_input(list_to_update, update_preferences=False):
    updated = False
    while True:
        item = input().strip().capitalize()
        if item == "":
            break

        if len(item) > max_table_width-6:
            print(f"Item not added - cannot be more than {max_table_width-6} characters. Try again.")
        else: 
            list_to_update.append(item)
            updated = True
            if update_preferences:
                set_preference(item, "")
            os.system("clear")
            print(f"{item} successfully added. Enter another or hit ENTER to return to menu.")
    os.system("clear")
    return list_to_update, updated

people_file = FileManager.PeopleFileManager(people_file)
people = people_file.get_people_from_file()

drinks_file = FileManager.DrinksFileManager(drinks_file)
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
        print(print_single_column_table("People", people))
        input("Hit ENTER to return to menu.")

    elif command == "2":
        print(print_single_column_table("Drinks", drinks))
        input("Hit ENTER to return to menu.")

    elif command == "3":
        print("Please enter a name to add. Hit enter when done to add another. ")
        people, success = take_list_input(people)
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
        names, drink_names = table_maker.extract_people_and_drinks(people)
        print(table_maker.print_single_column_table("People", names))
        print("To set a favourite drink, enter the ID of a person.")
        name_id = input("Enter an ID: ")
        if name_id == "":
            continue
        try:
            name_id = int(name_id)
            assert name_id in range(1,len(names)+1)
        except:
            print(f"ID {name_id} not recognised. Hit ENTER to return to menu.")
            input()
            os.system("clear")
            continue

        drink_names = table_maker.extract_drinks_names(drinks)
        print(table_maker.print_single_column_table("Drinks", drink_names))
        print("Now enter the ID of the favourite drink.")
        drink_id = input("Enter an ID: ")
        if drink_id == "":
            continue
        try:
            drink_id = int(drink_id)
            assert drink_id in range(1,len(drink_names)+1)
        except:
            print(f"ID {drink_id} not recognised. Hit ENTER to return to menu.")
            input()
            os.system("clear")
            continue

        set_preference(name_id, drink_id)
        updated_preferences = True

        os.system("clear")
        print(f"{get_person_from_id(name_id)}'s favourite drink is now {get_drink_from_id(drink_id)}.\n")
        input("Hit ENTER to return to menu.")

    elif command.lower() == "e":
        break

    else: 
        print("Unrecognised command. ")
    os.system("clear")

if updated_people:
    update_list_file(people_file, people)
if updated_drinks:
    update_list_file(drinks_file, drinks)
if updated_preferences:
    update_dict_file(preferences_file, preferences)