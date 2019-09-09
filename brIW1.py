import sys
import os
import random

args = sys.argv
help = f"""HELP: brIW helps you collect drinks rounds. To start, just enter
    python3 {args[0]}
"""
if len(args) > 1:
    if args[1] == "-h":
        print(help)
    else:
        print("No arguments needed for this program (yet!). For help use -h.")
    exit()

menu = """
============== MENU ==============

    [1] Get all people
    [2] Get all drinks
    [3] Add people
    [4] Add drinks
    [5] Get favourite drinks
    [6] Set favourite drinks
    [E] Save & Exit
"""
welcome = "Welcome to BrIW v0.1!"
people_file = "./people.txt"
drinks_file = "./drinks.txt"
preferences_file = "./preferences.txt"
max_table_width = 90

def ask_to_continue(message):
    while True:
        print(f"{message} \nContinue anyway? (y/n)")
        choice = input().lower()
        if choice == "y":
            break
        elif choice == "n":
            exit()
        else:
            print("Unrecognised input. ")

def update_list_file(list_file, updated_list):
    # Overwrites whole file (TODO: not this)
    with open(list_file,"w") as file:
        for item in updated_list:
            file.write(f"{item}\n")

def update_dict_file(dict_file, updated_dict):
    with open(dict_file,"w") as file:
        for key in updated_dict:
            file.write(f"{key}:{updated_dict[key]}\n")

def read_list_file(file_name):
    assert file_name != "", "No file supplied."

    items = []
    with open(file_name,"rt",newline="\n") as file:
        for line in file:
            if line[:-1] != "":
                items.append(line[:-1].capitalize())
    
    if len(items) == 0:
        ask_to_continue(f"Empty file supplied: {file_name}")

    return items

def read_dict_file(file_name):
    lines = read_list_file(file_name)
    new_dict = {}
    for line in lines:
        key, value = line.split(":")
        new_dict[key] = value
    return new_dict

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

def calculate_column_width(rows):
    longest_item = 0
    for item in rows:
        if len(item) > longest_item:
            longest_item = len(item)
    
    if longest_item+6 > 20:
        return longest_item+6
    return 20

def make_row(text, table_width, use_index=True, index=""):
    if use_index:
        return "| {} {}{} |\n".format(index, text, " "*(table_width-6-len(text)))
    else:
       return "| {}{} |\n".format(text, " "*(table_width-4-len(text)))

def make_table_break(table_width):
    return "+{}+\n".format("-"*(table_width-2))

def _print_as_table(header, rows, table_width, use_index):
    text = make_table_break(table_width) + make_row(header, table_width, use_index, index=" ") + make_table_break(table_width)
    for index in range(len(rows)):
        text += make_row(rows[index], table_width, use_index, index=index+1)
    text += make_table_break(table_width)
    return text

def print_1column_table(header, rows):
    return _print_as_table(header, rows, calculate_column_width(rows), True)

def print_preferences(preferences):
    names_width = calculate_column_width(people)-6
    drinks_width = calculate_column_width(drinks)-6
    header = "Person{} | Fav Drink {}".format(" "*(names_width-7), " "*(drinks_width-11))
    rows = []
    for name_id in preferences:
        name = get_person_from_id(name_id)
        drink = get_drink_from_id(preferences[name_id])
        rows.append("{}{} | {}{}".format(name, " "*(names_width-len(name)-1), drink, " "*(drinks_width-len(drink)-1)))
    return _print_as_table(header, rows, calculate_column_width(rows), False)

def take_list_input(list_to_update):
    updated = False
    while True:
        item = input().strip()
        if item == "":
            break

        if len(item) > max_table_width-6:
            print(f"Item not added - cannot be more than {max_table_width-6} characters. Try again.")
        else: 
            list_to_update.append(item.capitalize())
            updated = True
            os.system("clear")
            print(f"{item} successfully added. Enter another or hit ENTER to return to menu.")
    os.system("clear")
    return list_to_update, updated

people = read_list_file(people_file)
start_num_of_people = len(people)

drinks = read_list_file(drinks_file)
start_num_of_drinks = len(drinks)

preferences = {}
for index in range(len(people)):
    # Assign a random favourite drink for now
    preferences[index] = random.randint(0,len(drinks)-1)

updated_people, updated_drinks, updated_preferences = False, False, False

os.system("clear")
print(welcome)

while True:
    print(menu)
    command = input("Enter a number to select a command: ")
    os.system("clear")
    if len(command) == 0:
        print("Expected input, none provided. ")

    elif command == "1":
        print(print_1column_table("People", people))
        input("Hit ENTER to return to menu.")

    elif command == "2":
        print(print_1column_table("Drinks", drinks))
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
        print(print_preferences(preferences))
        input("Hit ENTER to return to menu.")

    elif command == "6":
        print(print_1column_table("People", people))
        print("To set a favourite drink, enter the ID of a person.")
        try:
            name_id = int(input("Enter an id: "))
            assert name_id in range(1,len(people)+1)
        except:
            print(f"ID {name_id} not recognised. Hit ENTER to return to menu.")
            input()
            os.system("clear")
            continue

        print(print_1column_table("Drinks", drinks))
        print("Now enter the id of the favourite drink.")
        try:
            drink_id = int(input("Enter an id: "))
            assert drink_id in range(1,len(drinks)+1)
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