FROM python:3.8-slim-buster

RUN pip install --upgrade pip

ADD main.py main.py
ADD requirements.txt requirements.txt

RUN pip install -r requirements.txt

CMD [ "python", "./main.py" ]