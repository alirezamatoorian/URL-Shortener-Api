from python:3.14-slim

WORKDIR /app





CMD["python","manage.py","runserver","0.0.0.0:8000"]