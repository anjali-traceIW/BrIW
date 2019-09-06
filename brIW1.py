import sys
import os

commands = """
Please enter a number to select a command:

    [1] Get all people
    [2] Get all drinks
    [3] Add people
    [4] Add drinks
    [5] Exit
"""
welcome = "Welcome to BrIW v0.1!"
people_file = "./people.txt"
drinks_file = "./drinks.txt"

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


def read_list_file(file_name):
    assert file_name != "", "No file supplied."

    items = []
    with open(file_name,"rt",newline="\n") as file:
        for line in file:
            if line[:-1] != "":
                items.append(line[:-1])

    if len(items) == 0:
        ask_to_continue(f"Empty file supplied: {file_name}")

    return items

def calculate_width(rows):
    longest_item = 0
    for item in rows:
        if len(item) > longest_item:
            longest_item = len(item)
    
    if longest_item+4 > 20:
        return longest_item+4
    return 20

def make_row(text, table_width):
    return "| {}{} |\n".format(text.capitalize(), " "*(table_width-4-len(text)))

def print_as_table(header, rows):
    table_width = calculate_width(rows)
    table_break = "+{}+\n".format("-"*(table_width-2))
    text = table_break + make_row(header, table_width) + table_break
    for item in rows:
        text += make_row(item, table_width)
    text += table_break
    print(text)

# people = ["Scooby Dooooooooooooooooooo", "Shaggy", "Fred", "Daphne", "Velma"]
# drinks = ["coffee", "tea", "lemonade"]

people = read_list_file(people_file)
start_num_of_people = len(people)
drinks = read_list_file(drinks_file)
start_num_of_drinks = len(drinks)

os.system("clear")
print(welcome)

while True:
    print(commands)
    command = input()
    os.system("clear")
    if len(command) == 0:
        print("Expected input, none provided. ")
    elif command == "1":
        print_as_table("People", people)
    elif command == "2":
        print_as_table("Drinks", drinks)
    elif  command == "3":
        print("Please enter a name to add: ")
        name = input()
        people.append(name)
        os.system("clear")
        print(f"{name} successfully added to people.")
    elif command == "4":
        print("Please enter a drink to add: ")
        drink = input()
        os.system("clear")
        drinks.append(drink)
        print(f"{drink} successfully added to drinks.")
    elif command == "5":
        exit()
    else: 
        print("Unrecognised command. ")
