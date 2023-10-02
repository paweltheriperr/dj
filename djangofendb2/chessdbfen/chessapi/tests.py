import time
from testcontainers.mysql import MySqlContainer

def test_mysql_container():
    mysql_container = MySqlContainer()
    mysql_container.start()

    # Oczekuj na gotowość kontenera, np. sprawdzając, czy jest dostępny port 3306
    while True:
        try:
            mysql_container.get_connection_url()
            break
        except Exception as e:
            print(f"Waiting for MySQL container: {e}")
            time.sleep(1)

    # Tutaj możesz przeprowadzić swoje testy

    mysql_container.stop()
