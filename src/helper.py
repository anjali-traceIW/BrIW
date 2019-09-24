import os
# from cls.Person import People
# from cls.Drink import Drinks

def ask_a_question_to_continue(message):
    while True:
        print(f"{message} (y/n)")
        choice = input().lower()
        if choice == "y":
            return True
        elif choice == "n":
            return False
        else:
            print("Unrecognised input. ")

def check_a_name(name, people):
    if not people.check_person_exists(name):
        print(f"Person {name} not recognised. Hit ENTER and try again.")
        input()
        os.system("clear")
        return False
    return True

def check_a_drink(drink_name, drinks):
    if not drinks.check_drink_exists(drink_name):
        print(f"Drink {drink_name} not recognised. Hit ENTER to start again.")
        input()
        os.system("clear")
        return False
    return True