import unittest
from unittest.mock import MagicMock
from src.cls.DbManager import *
from src.brIW1 import App

class Test_integration(unittest.TestCase):

    def test_get_drinks_from_db_on_startup(self):
        drinks_db_mock = MagicMock(wraps=DrinksDbManager)
        # App initialisation requires actual drinks list to set up rounds, so 
        # mock that too while we're not mocking the other db managers
        mock_drinks = Drinks([Drink("Coffee"), Drink("Tea"), Drink("Lemonade")])
        drinks_db_mock.get_all_drinks.side_effect = [mock_drinks]

        app = App(PeopleDbManager, drinks_db_mock, RoundsDbManager)

        drinks_db_mock.get_all_drinks.assert_called()


    # def test_update_drinks_in_db_on_exit(self):
    #     drinks_db_mock = MagicMock(wraps=DrinksDbManager)    
    #     app = App(PeopleDbManager, drinks_db_mock, RoundsDbManager)

    #     app.exit(False, True, False)

    #     drinks_db_mock.update_drinks.assert_called()



    # def test_get_rounds_endpoint_calls_get_peeps_from_db(self):
    #     rounds_db = MagicMock(wraps=RoundsDbManager)

    #     RoundsHandler.do_POST(rounds_db)

    #     # rounds_db.

if __name__ == "__main__": 
	unittest.main()