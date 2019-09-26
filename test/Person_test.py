import unittest

from src.cls.Person import Person, People
from src.cls.Drink import Drink

class Test_People(unittest.TestCase):

	def test_make_empty_person(self):
		# Arrange
		expected_name, expected_drink = "", Drink("") 

		# Act
		person = Person("")

		# Assert
		self.assertEqual(expected_name, person.name)
		self.assertEqual(expected_drink, person.favourite_drink)

	def test_make_a_person_with_no_fav_drink(self):
		expected_name, expected_drink = "Janet", Drink("") 

		person = Person("janet")

		self.assertEqual(expected_name, person.name)
		self.assertEqual(expected_drink, person.favourite_drink)

	def test_make_a_person_with_a_fav_drink(self):
		expected_name, expected_drink = "Brad", Drink("milkshake") 
		expected_person = Person(expected_name, expected_drink)

		actual_person = Person("brad", Drink("milkshake"))

		self.assertEqual(expected_person, actual_person)

	def test_make_a_person_without_args(self):
		with self.assertRaises(Exception):
			Person()

	def test_make_a_person_with_a_str_drink(self):
		with self.assertRaises(TypeError):
			Person("Rocky", "Jam")

	def test_make_a_person_with_whitespace_lower_name(self):
		expected_name = "Janet"

		person = Person("      janet     ")
		self.assertEqual(expected_name, person.name)

	def test_change_fav_drink_for_person(self):
		expected_person = Person("Meatloaf", Drink("Orange Juice"))

		actual_person = Person("Meatloaf", Drink("Hot chocolate"))
		actual_person.favourite_drink = Drink("Orange juice")

		self.assertEqual(expected_person, actual_person)



	# ==== TESTING PEOPLE CLASS BELOW ====

	def test_make_empty_people(self):
		expected_all_people = {}
		people = People()

		self.assertEqual(people.all_people, expected_all_people)

	def test_add_person(self):
		expected_people = People()
		expected_people.all_people = {"Bob": Person("Bob"), "Wendy": Person("Wendy")}

		actual_people = People()
		actual_people.add_person(Person("Bob"))
		actual_people.add_person(Person("Wendy"))

		self.assertEqual(expected_people, actual_people)
		
	def test_add_multiple_people(self):
		expected_people = People()
		expected_people.all_people = {"Bob": Person("Bob"), "Wendy": Person("Wendy")}

		actual_people = People()
		actual_people.add_people([Person("Bob"), Person("Wendy")])

		self.assertEqual(expected_people, actual_people)

	def test_people_get_names(self):
		expected_names = ["Bob", "Wendy"]

		people = People()
		people.add_person(Person("Bob"))
		people.add_person(Person("Wendy"))

		self.assertEqual(people.get_names(), expected_names)

if __name__ == "__main__":
    unittest.main()