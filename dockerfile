    FROM python:3.9-alpine
    WORKDIR /usr/src/app
    COPY . .
    CMD ["python","Dijkstra.py"]