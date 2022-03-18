FROM python:3.8

RUN pip install django
RUN pip install psycopg2-binary

ADD . /src
WORKDIR /src
CMD python ./manage.py runserver 0.0.0.0:8000
