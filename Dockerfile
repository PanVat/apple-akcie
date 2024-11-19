# Základní obraz pro Python
FROM python:3.11-slim
# Nastavení pracovního adresáře
WORKDIR /app
# Kopírování souboru se závislostmi do pracovního adresáře
COPY requirements.txt .
# Instalace všech závislostí ze souboru `requirements.txt`
RUN pip install --no-cache-dir -r requirements.txt
# Kopírování všech souborů aplikace do kontejneru
COPY . .
# Otevření portu, na kterém běží Flask
EXPOSE 5000
# Spuštění aplikace na všech dostupných IP adresách
CMD ["flask", "run", "--host=0.0.0.0"]