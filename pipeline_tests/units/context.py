import unittest
from app.run import conf, environment

class UtilsTest(unittest.TestCase):
    def setUp(self):
        pass

    def load_file(self):
        load_file = 'data'
        self.assertEqual('data', loaded_file)


    def load_db(self):
        load_db = 'data'
        self.assertEqual('data', loaded_db)


    def save_db(self):
        save_db = 'data'
        self.assertEqual('data', save_db)
