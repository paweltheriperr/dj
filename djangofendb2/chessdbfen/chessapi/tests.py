#from django.test import TestCase
#from testcontainers.postgres import PostgresContainer
#import psycopg2
#from .models import Fen
#
#class FenModelTestCase(TestCase):
#    def setUp(self):
#        # Uruchom kontener Postgres
#        self.container = PostgresContainer("postgres:latest")
#        self.container.start()
#
#        # Pobierz dane do połączenia z bazą danych z kontenera
#        self.db_params = {
#            'database': self.container.get_database_name(),
#            'user': self.container.get_username(),
#            'password': self.container.get_password(),
#            'host': self.container.get_container_host_ip(),
#            'port': self.container.get_exposed_port(5432),
#        }
#
#    def tearDown(self):
#        # Zatrzymaj kontener Postgres po zakończeniu testu
#        self.container.stop()
#
#    def test_fen_model(self):
#        # Przykładowy test dotyczący modelu Django "Fen"
#        # Tworzymy instancję modelu i zapisujemy ją w bazie danych
#        fen_instance = Fen(fen="Test FEN")
#        fen_instance.save()
#
#        # Sprawdzamy, czy instancja została poprawnie zapisana w bazie danych
#        retrieved_fen = Fen.objects.get(fen="Test FEN")
#        self.assertEqual(retrieved_fen.fen, "Test FEN")
from django.test import TestCase
from .models import Fen

class FenModelTestCase(TestCase):
    def test_create_fen(self):
        # Tworzenie instancji modelu Fen
        fen = Fen(fen="Test FEN")
        fen.save()

        # Sprawdzanie, czy instancja została poprawnie zapisana w bazie danych
        saved_fen = Fen.objects.get(fen="Test FEN")
        self.assertEqual(saved_fen.fen, "Test FEN")

    def test_fen_blank_field(self):
        # Test, czy pole "fen" może być puste (blank=True)
        fen = Fen()
        fen.save()

        # Sprawdzanie, czy instancja została poprawnie zapisana w bazie danych
        saved_fen = Fen.objects.get(pk=fen.pk)
        self.assertEqual(saved_fen.fen, "")

    def test_added_auto_now_add(self):
        # Test, czy pole "added" jest automatycznie wypełniane datą utworzenia
        fen = Fen(fen="Test FEN")
        fen.save()

        # Sprawdzanie, czy pole "added" nie jest puste
        saved_fen = Fen.objects.get(pk=fen.pk)
        self.assertIsNotNone(saved_fen.added)
