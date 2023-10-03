from django.urls import reverse
from django.test import Client, TestCase
from .models import Fen  # Assuming that your models are in the same module as this test file
import time
import pytest
from testcontainers.mysql import MySqlContainer

class TestKurwy(TestCase):
    @pytest.fixture(scope="module")
    def mysql_container(self):
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

        yield mysql_container

        mysql_container.stop()

    def test_get_latest_fen(self):
        client = Client()
        # Tworzymy przykładowe dane w bazie danych
        Fen.objects.create(fen="example_fen_data")

        # Wywołujemy widok get_latest_fen
        url = reverse("get_latest_fen")  # Assuming "get_latest_fen" is a valid URL name
        response = client.get(url, content_type="application/json")

        # Sprawdzamy, czy odpowiedź ma status HTTP 200 OK
        self.assertEqual(response.status_code, 200)

        # Sprawdzamy, czy otrzymane dane są zgodne z danymi w bazie danych
        latest_fen = Fen.objects.latest("added")
        self.assertEqual(response.json()["fen"], latest_fen.fen)
