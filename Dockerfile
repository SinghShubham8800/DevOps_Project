FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# This line is the fix! It copies app.py AND the templates folder
COPY . .

CMD ["python", "app.py"]
