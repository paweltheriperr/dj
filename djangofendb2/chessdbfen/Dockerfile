# Używamy oficjalnego obrazu Pythona
FROM python:3.9

# Ustalamy zmienną środowiskową PYTHONUNBUFFERED na 1, aby uniknąć buforowania wyjścia
ENV PYTHONUNBUFFERED 1

# Tworzymy katalog /app jako katalog roboczy w kontenerze
WORKDIR /chessdbfen

# Kopiujemy plik requirements.txt do kontenera
COPY requirements.txt /chessdbfen/

# Instalujemy zależności Pythona
RUN pip install -r requirements.txt

# Kopiujemy resztę projektu do kontenera
COPY . /chessdbfen/
