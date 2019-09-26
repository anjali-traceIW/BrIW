import sys
import os
import random
from src.cls.Round import Round
from src.cls.Person import Person
from src.cls.Drink import Drink 
from src.cls.FileManager import PeopleFileManager, DrinksFileManager, RoundsFileManager
from src.cls.DbManager import PeopleDbManager, DrinksDbManager, RoundsDbManager
from prettytable import PrettyTable
import src.table_maker as table_maker
import src.helper as helper
from datetime import datetime

class App:
    def __init__(self, PeopleDbManager, DrinksDbManager, RoundsDbManager):
        self.people_file_path = "data/people.csv"
        self.drinks_file_path = "data/drinks.csv"
        self.rounds_file_path = "data/rounds.csv"
        self.max_table_width = 90

        self.drinks_file = DrinksFileManager(self.drinks_file_path)
        # self.drinks = self.drinks_file.get_drinks_from_file()
        self.drinks = DrinksDbManager.get_all_drinks()

        self.people_file = PeopleFileManager(self.people_file_path)
        self.all_people = self.people_file.get_people_from_file()
        # self.all_people = self.people_file.get_people_from_db(self.drinks)

        self.rounds_file = RoundsFileManager(self.rounds_file_path)
        self.rounds = self.rounds_file.get_rounds_from_file(self.all_people, self.drinks)


    def exit(self, updated_people, updated_drinks, updated_rounds):
        if updated_people:
            self.people_file.update_file(self.all_people)
            
        if updated_drinks:
            self.drinks_file.update_file(self.drinks)
            
        if updated_rounds:
            self.rounds_file.update_file(self.rounds)


    def take_list_input(self, list_to_update, max_table_width, update_preferences=False):
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


    def main(self):
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
        
        # http://patorjk.com/software/taag/#p=display&f=ANSI%20Shadow&t=BrIW%200.1
        menu = r"""
    ██████╗       ██╗██╗    ██╗     ██████╗     ██╗
    ██╔══██╗      ██║██║    ██║    ██╔═████╗  ████║
    ██████╔╝█████╗██║██║ █╗ ██║    ██║██╔██║  ╚═██║
    ██╔══██╗██╔══╝██║██║███╗██║    ████╔╝██║    ██║
    ██████╔╝██║   ██║╚███╔███╔╝    ╚██████╔╝██╗ ██║
    ╚═════╝ ╚═╝   ╚═╝ ╚══╝╚══╝      ╚═════╝ ╚═╝ ╚═╝

                                            {
    [1] Get all people                     {   }
    [2] Get all drinks                      }_{ __{
    [3] Add people                       .-{   }   }-.
    [4] Add drinks                      (   }     {   )
                                        |`-.._____..-'|
    [5] Get favourite drinks            |             ;--.
    [6] Set favourite drinks            |            (__  \\
                                        |             | )  )
    [7] Start a round                   |             |/  /
    [8] View rounds                     |             /  / 
                                        |            (  /
    [E] Save & Exit                     \             y'
                                        `-.._____..-'
        """
        welcome = "Welcome to BrIW v0.1!"
        updated_people, updated_drinks, updated_rounds = False, False, False

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
                print(table_maker.print_single_column_table("People", self.all_people.get_names()))
                input("Hit ENTER to return to menu.")

            elif command == "2":
                print(table_maker.print_single_column_table("Drinks", self.drinks.get_names()))
                input("Hit ENTER to return to menu.")

            elif command == "3":
                print("Please enter a name to add. Hit enter when done to add another. ")
                self.all_people, success = self.take_list_input(self.all_people, True)
                if success:
                    updated_people = True

            elif command == "4":
                print("Please enter a drink to add: ")
                self.drinks, success = self.take_list_input(self.drinks)
                if success:
                    updated_drinks = True

            elif command == "5":
                print(table_maker.print_people_drinks(self.all_people))
                input("Hit ENTER to return to menu.")

            elif command == "6":
                print(table_maker.print_single_column_table("People", self.all_people.get_names()))
                print("To set a favourite drink, enter the name of a person.")
                name = input("Enter a name: ").capitalize()
                if name == "":
                    continue
                elif not helper.check_a_name(name, self.all_people):
                    continue
                person = self.all_people.get_person(name)

                print(table_maker.print_single_column_table("Drinks", self.drinks.get_names()))
                print("Now enter the name of their favourite drink.")
                drink_name = input("Enter a drink name: ").capitalize()
                if drink_name == "":
                    continue
                elif not helper.check_a_drink(drink_name, self.drinks):
                    continue
                drink = self.drinks.get_drink(drink_name)
                
                person.favourite_drink = drink
                self.all_people.update_person(person)
                updated_people, updated_drinks = True, True
                os.system("clear")
                print(f"{name}'s favourite drink is now {drink_name}.\n")
                input("Hit ENTER to return to menu.")

            elif command == "7":
                # print ("Making a new round.")
                print("Who's making the brews this round?")
                name = input("Enter the brewer's name: ").capitalize()
                if not helper.check_a_name(name, self.all_people):
                    continue
                round = Round(self.all_people.get_person(name), datetime.now())
                updated_rounds = True
                if not helper.ask_a_question_to_continue("Start the round now?"):
                    self.rounds.add_round(round)
                    continue
                round.active = True
                while True:
                    print("To add someone to this round, please enter their name. Else hit ENTER to return to menu.")
                    name = input().capitalize()
                    if name == "":
                        break
                    if not helper.check_a_name(name, self.all_people):
                        continue

                    person = self.all_people.get_person(name)
                    fav_drink = person.favourite_drink
                    if helper.ask_a_question_to_continue(f"{name}'s favourite drink is {fav_drink.name}. Is this their order?"):
                        round.add_order(person, fav_drink)
                        print(f"Added {person.name}'s order of {fav_drink.name} to round.")
                        continue

                    print(f"What drink would {name} like?")
                    drink_name = input().capitalize()
                    if not helper.check_a_drink(drink_name, self.drinks):
                        continue
                    drink = self.drinks.get_drink(drink_name)
                    round.add_order(person, drink)
                    print(f"Added {person.name}'s order of {drink.name} to round.")
                self.rounds.add_round(round)
                print("This round: ")
                print(round)
                input("Hit ENTER to return to menu.")

            elif command == "8":
                for round in self.rounds.all_rounds:
                    print(round)
                input("Hit ENTER to return to menu.")

            elif command.lower() == "e":
                print("Closing app...")
                self.exit(updated_people, updated_drinks, updated_rounds)
                break

            else: 
                print("Unrecognised command. ")
            os.system("clear")
        print("Come back soon!")

if __name__ == "__main__":
    app = App(PeopleDbManager, DrinksDbManager, RoundsDbManager)
    app.main()