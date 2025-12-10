FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN apt-get update \
 && apt-get install -y pkg-config default-libmysqlclient-dev gcc \
 && pip install --no-cache-dir -r requirements.txt \
 && apt-get clean && rm -rf /var/lib/apt/lists/*

COPY . .

ENV PORT=5000
EXPOSE 5000

CMD ["gunicorn", "--workers", "2", "--threads", "4", "--bind", "0.0.0.0:5000", "application:application"]
