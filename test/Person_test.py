import unittest

from src.cls.Person import *
from src.cls.Drink import Drink

class Test_People(unittest.TestCase):

	def test_make_empty_person(self):
		# Arrange
		expected_name, expected_drink = "", Drink("") 

		# Act
		person = Person("")

		# Assert
		self.assertEquals(expected_name, person.name)
		self.assertEquals(expected_drink, person.favourite_drink)

	def test_make_a_person_with_no_fav_drink(self):
		expected_name, expected_drink = "Janet", Drink("") 

		person = Person("janet")

		self.assertEquals(expected_name, person.name)
		self.assertEquals(expected_drink, person.favourite_drink)

	def test_make_a_person_with_a_fav_drink(self):
		expected_name, expected_drink = "Brad", Drink("milkshake") 
		expected_person = Person(expected_name, expected_drink)

		actual_person = Person("brad", Drink("milkshake"))

		# self.assertEquals(expected_name, person.name)
		# self.assertEquals(expected_drink, person.favourite_drink)
		self.assertEquals(expected_person, actual_person)

if __name__ == "__main__":
    unittest.main()