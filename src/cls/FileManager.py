import helper
#from cls import Person, Drink
from cls.Person import Person, People
from cls.Drink import Drink, Drinks

class FileManager:

    def __init__(self, file_path):
        assert file_path != "", "No file supplied."
        self.file_path = file_path

    def read_file(self):
        items = []
        with open(self.file_path,"rt",newline="\n") as file:
            for line in file:
                if line[:-1] != "":
                    items.append(line[:-1].capitalize())

        if len(items) == 0:
            helper.ask_to_continue(f"Empty file supplied: {self.file_path}")

        return items

    def overwrite_file(self, new_lines):
        with open(self.file_path,"w") as file:
            for line in new_lines:
                file.write(f"{line}\n")
    
class PeopleFileManager(FileManager):

    # def __init__(self, file_path):
    #     self.file_path = file_path

    def get_people_from_file(self):
        people = People()
        rows = FileManager.read_file(self)
        for row in rows:
            new_row = [x.strip() for x in row.split(',')]
            people.add_person(Person(new_row[0], Drink(new_row[1])))
        self.start_no_of_people = len(people.get_names())
        return people

    def update_file(self, updated_people):
        rows = []
        for person in updated_people.values():
            rows.append(person.make_csv_line())
        FileManager.overwrite_file(self, rows)

class DrinksFileManager(FileManager):

    # def __init__(self, file_path):
    #     self.file_path = file_path

    def get_drinks_from_file(self):
        drinks = Drinks()
        rows = FileManager.read_file(self)
        for row in rows:
            drinks.add_drink(Drink(row))
        self.start_no_of_drinks = len(drinks.get_names())
        return drinks

    def update_file(self, updated_drinks):
        rows = []
        for drink in updated_drinks.values():
            rows.append(drink.make_csv_line())
        FileManager.overwrite_file(self, rows)