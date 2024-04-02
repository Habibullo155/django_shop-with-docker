FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


WORKDIR /app

COPY requirements.txt /app/

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install django-environ

COPY ./myproject /app/
COPY ./main /app/
COPY ./goods /app/
COPY ./static /app/
COPY ./users /app/
COPY ./templates /app/

CMD python manage.py runserver 0.0.0.0:8000
