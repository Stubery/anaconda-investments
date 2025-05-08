import sqlite3
import unittest

from tests.utils.test_utils import fetch_resource_path


class DatabaseTestCase(unittest.TestCase):
    def test_database_connection(self):

        resource_path = "investments.db"
        db_path = fetch_resource_path(resource_path)

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
