from python:3.14-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app

RUN useradd -m appuser && chown -R appuser:appuser /app
USER appuser


EXPOSE 8000


RUN python manage.py collectstatic --noinput

#CMD ["python","manage.py","runserver","0.0.0.0:8000"]