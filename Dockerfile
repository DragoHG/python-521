
FROM python:3.6.7

WORKDIR /app

ADD . /app

RUN pip install -r requirements.txt

CMD [ "python", "app.py" ]

