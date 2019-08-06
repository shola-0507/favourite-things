FROM python:3.7.2-stretch

WORKDIR /usr/src/backend

COPY ./requirements.txt ./

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY . .

CMD ["uwsgi", "app.ini"]