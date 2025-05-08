import sqlite3
import unittest

class DatabaseTestCase(unittest.TestCase):
    def test_database_connection(self):
        sqlite_connection = sqlite3.connect('..\\resources\\investments.db')
        cursor = sqlite_connection.cursor()
        query = 'SELECT * FROM equity_prices LIMIT 10;'
        cursor.execute(query)
        result = cursor.fetchall()
        assert len(result) == 10

if __name__ == '__main__':
    unittest.main()
