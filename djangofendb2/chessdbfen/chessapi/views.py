# views.py

# Importuj moduły, które pomagają nam komunikować się z resztą świata.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Teraz przyszła pora na model danych - jak książka, ale bez opowieści.
from .models import Fen
# Serializer, który zamienia nasze książki na coś bardziej przystępnego - jak tłumaczenie książki na inny język.
from .serializers import FenSerializer


# Definiujemy widok, który pozwala na zapisywanie danych, ale tylko jeśli ktoś użyje metody POST.
@api_view(['POST'])
def save_fen(request):
    # No dobrze, ktoś próbuje nas odwiedzić!
    if request.method == 'POST':
        # Tworzymy tłumacza, który przetłumaczy dane na coś bardziej zrozumiałego.
        serializer = FenSerializer(data=request.data)
        # Sprawdzamy, czy tłumaczenie jest poprawne.
        if serializer.is_valid():
            # Jeśli tak, to zapisujemy je.
            serializer.save()
            # I mówimy odwiedzającemu, że wszystko poszło gładko.
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # Jeśli tłumaczenie było beznadziejne, to mówimy o tym odwiedzającemu.
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Kolejny widok, tym razem do czytania danych.
@api_view(['GET'])
def get_latest_fen(request):
    try:
        # Szukamy najnowszego wpisu - jak próba znalezienia najnowszej mody w świecie mody.
        latest_fen = Fen.objects.latest('added')
        # Tworzymy tłumacza, żebyśmy mogli zrozumieć naszą najnowszą mody.
        serializer = FenSerializer(latest_fen)
        # I pokazujemy ją odwiedzającym, jak nową suknię na wybiegu.
        return Response(serializer.data)
    except Fen.DoesNotExist:
        # No cóż, wygląda na to, że nie mamy jeszcze nowych mód. Szukamy dalej!
        return Response({}, status=status.HTTP_404_NOT_FOUND)
