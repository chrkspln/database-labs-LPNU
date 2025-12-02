FROM python:3.9-slim
WORKDIR /backend
COPY requirements.txt .
RUN apt-get update && apt-get install -y pkg-config default-libmysqlclient-dev gcc \
    && pip install --no-cache-dir -r requirements.txt \
    && apt-get clean && rm -rf /var/lib/apt/lists/*
COPY . .
EXPOSE 5000
CMD ["flask","run", "--host", "0.0.0.0"]