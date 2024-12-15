# Użyj obrazu bazowego z Pythonem
FROM python:3.9

# Ustaw katalog roboczy
WORKDIR /app

# Skopiuj plik requirements.txt i zainstaluj zależności
COPY requirements.txt .

RUN pip install -r requirements.txt

# Skopiuj kod aplikacji
COPY . .

# Ustaw port aplikacji
EXPOSE 5000

# Polecenie uruchamiające aplikację
CMD ["python", "app.py"]
