FROM python:3.12-slim as installer

WORKDIR /app
COPY requirements.txt ./
RUN pip install -r requirements.txt

FROM installer

WORKDIR /app
COPY . .
EXPOSE 5000

CMD ["python", "server.py"]