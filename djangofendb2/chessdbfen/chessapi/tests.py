import unittest
from testcontainers.mysql import MySqlContainer
from sqlalchemy import create_engine


class TestCustomMySQLContainer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        # Dostosowanie kontenera MySQL do wymagań
        mysql_custom = MySqlContainer(
            "mysql:8.0",
            user="customuser",
            password="custompassword",
            database="customdb"
        )
        cls.container = mysql_custom
        cls.container.start()

        # Tworzenie połączenia SQLAlchemy do kontenera
        cls.engine = create_engine(cls.container.get_connection_url())

    @classmethod
    def tearDownClass(cls):
        cls.container.stop()
        super().tearDownClass()

    def test_database_connection(self):
        # Przykład testu, który sprawdza połączenie z dostosowanym kontenerem MySQL
        with self.engine.connect() as conn:
            result = conn.execute("SELECT 1")
            self.assertEqual(result.scalar(), 1)


if __name__ == '__main__':
    unittest.main()
