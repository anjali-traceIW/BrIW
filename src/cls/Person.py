class Person:

    def __init__(self, name, fav_drink=""):
        self.name = name.strip().capitalize()
        self.favourite_drink = fav_drink

    def make_csv_line(self):
        return f"{self.name},{self.favourite_drink.name}\n"

class People:

    def __init__(self, people=[]):
        self.all_people = {}
        self.add_people(people)

    def add_person(self, person):
        if self.check_person_exists(person.name):
            raise Exception(f"Person {person.name} already exists.")
        self.all_people[person.name] = person
    
    def add_people(self, people):
        for person in people:
            self.add_person(person)

    def get_person(self, name):
        return self.all_people[name]

    def update_person(self, person):
        self.all_people[person.name] = person

    def get_names(self):
        return list(self.all_people.keys())

    def get_fav_drinks(self):
        fav_drinks = []
        for person in self.all_people.values():
            fav_drinks.append(person.favourite_drink.name)
        return fav_drinks

    def check_person_exists(self, name):
        return name in self.all_people.keys()
