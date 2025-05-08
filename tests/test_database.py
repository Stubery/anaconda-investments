import os
import pathlib
import sqlite3
import unittest

class DatabaseTestCase(unittest.TestCase):
    def test_database_connection(self):

        db_path = "resources/investments.db" if os.getcwd().endswith("anaconda-investments") else "../resources/investments.db"


        print('CWD:     ', os.getcwd())
        print('Absolute path of file:     ', db_path)

        sqlite_connection = sqlite3.connect(db_path)
        cursor = sqlite_connection.cursor()

        query = 'SELECT * FROM sqlite_master WHERE type="table";'
        cursor.execute(query)
        result = cursor.fetchall()
        print(f"Tables: {result}")

        query = 'SELECT * FROM equity_prices LIMIT 10;'
        cursor.execute(query)
        result = cursor.fetchall()
        assert len(result) == 10

if __name__ == '__main__':
    unittest.main()
