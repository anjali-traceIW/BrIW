from src.cls.Drink import Drink

class Person:

    def __init__(self, name, fav_drink=Drink("")):
        self.name = name.strip().capitalize()
        if not isinstance(fav_drink, Drink):
            raise TypeError(f"Expected Drink object for favourite drink, received {type(fav_drink)}")
        self.favourite_drink = fav_drink

    def __eq__(self, other_person):
        return self.name == other_person.name and self.favourite_drink == other_person.favourite_drink

    def make_csv_line(self):
        return f"{self.name},{self.favourite_drink.name}"

class People:

    def __init__(self, people=[]):
        self.all_people = {}
        self.add_people(people)

    def __eq__(self, other_people):
        if len(self.all_people.keys()) != len(other_people.all_people.keys()):
            return False
        for person_name in self.all_people.keys():
            try: 
                if not self.get_person(person_name) == other_people.get_person(person_name):
                    # Both contain the person with name person_name, but different versions of it
                    return False
            except:
                # other_people does not contain one of the peoples' names
                return False
        return True

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
