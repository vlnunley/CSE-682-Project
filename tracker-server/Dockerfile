FROM python:3.12-slim AS installer

WORKDIR /app
COPY requirments.txt .
RUN pip install -r requirments.txt

FROM installer

WORKDIR /app
COPY . .
EXPOSE 5000

CMD ["python", "server.py"]