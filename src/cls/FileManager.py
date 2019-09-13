import helper
#from cls import Person, Drink
from cls.Person import Person
from cls.Drink import Drink

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

    def make_csv_line(self, content):
        line = ""
        for value in content:
            line = line + f"{value},"
        return line[-1]
    
class PeopleFileManager(FileManager):

    # def __init__(self, file_path):
    #     self.file_path = file_path

    def get_people_from_file(self):
        people = []
        rows = FileManager.read_file(self)
        for row in rows:
            new_row = [x.strip() for x in row.split(',')]
            people.append(Person(new_row[0], Drink(new_row[1])))
        self.start_no_of_people = len(people)
        return people

    def update_file(self, updated_people):
        rows = []
        for person in updated_people:
            rows.append(FileManager.make_csv_line(person))
        FileManager.overwrite_file(self, rows)

class DrinksFileManager(FileManager):

    # def __init__(self, file_path):
    #     self.file_path = file_path

    def get_drinks_from_file(self):
        drinks = []
        rows = FileManager.read_file(self)
        for row in rows:
            drinks.append(Drink(row))
        return drinks

    def update_file(self, updated_drinks):
        FileManager.overwrite_file(self, updated_drinks)