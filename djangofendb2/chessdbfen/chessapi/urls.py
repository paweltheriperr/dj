from django.urls import path
from . import views

urlpatterns = [
    # Inne ścieżki URL...
    path('api/save-fen/', views.save_fen, name='save_fen'),
    path('api/get-latest-fen/', views.get_latest_fen, name='get_latest_fen'),
]
