import unittest
from src.cls.FileManager import *

class Test_FileManger(unittest.TestCase):

    def test_make_a_generic_FileManager(self):
        self.assertIsInstance(FileManager("."), FileManager)

    def test_make_a_generic_FileManager_with_empty_filepath(self):
        with self.assertRaises(ValueError):
            manager = FileManager("")

    def test_make_a_generic_FileManager_with_no_args(self):
        with self.assertRaises(Exception):
            manager = FileManager()
