import unittest
import sqlite3
import os

class TestDatabase(unittest.TestCase):
    def test_databases_exist(self):
        self.assertTrue(os.path.exists('fruit_inventory.db'))
        self.assertTrue(os.path.exists('fruits_duration.db'))

    def test_fruit_inventory_table(self):
        conn = sqlite3.connect('fruit_inventory.db')
        cursor = conn.cursor()
        conn.close()
    
    def test_fruits_table(self):
        conn = sqlite3.connect('fruits_duration.db')
        cursor = conn.cursor()
        conn.close()

if __name__ == '__main__':
    unittest.main()