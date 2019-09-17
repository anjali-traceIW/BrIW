from src.cls.Drink import Drink

class Person:

    def __init__(self, name, fav_drink=Drink("")):
        self.name = name.strip().capitalize()
        self.favourite_drink = fav_drink

    def __eq__(self, other_person):
        return self.name == other_person.name and self.favourite_drink.is_equal(other_person.favourite_drink)

    def make_csv_line(self):
        return "{},{}".format(self.name,self.favourite_drink.name)

class People:

    def __init__(self, people=[]):
        self.all_people = {}
        self.add_people(people)

    def __eq__(self, other_people):
        if len(self.all_people.keys()) != len(other_people.all_people.keys()):
            return False
        for person_name in self.all_people.keys():
            try: 
                if not self.get_drink(person_name) == other_people.get_drink(person_name):
                    # Both contain the drink with name drink_name, but different versions of it
                    return False
            except:
                # other_drinks does not contain one of the drinks
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
