# A Python alap kép használata
FROM python:3.10-alpine

# Munkakönyvtár beállítása
WORKDIR /app

# Python fájlok másolása
COPY *.py /app/

# Webes fájlok másolása
COPY *.html /app/
COPY *.css /app/
COPY *.js /app/

# Szükséges Python csomagok telepítése
RUN pip install fastApi
RUN pip install uvicorn

# Port beállítása
EXPOSE 5000

# Alkalmazás futtatása
CMD ["python", "main_munkafeladat.py", "5000"]
