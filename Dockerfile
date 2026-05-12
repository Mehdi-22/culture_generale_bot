# Image Python + Playwright chromium (libs systeme installees via --with-deps)
FROM python:3.11-slim

WORKDIR /app

# Deps Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Navigateur chromium + dependances systeme (apt, en tant que root dans le build)
RUN playwright install --with-deps chromium

# Code applicatif
COPY . .

CMD ["python", "main.py"]
