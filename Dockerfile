FROM python:3.12

ENV PYTHONUNBUFFERED 1 
RUN mkdir /code
WORKDIR /code
ADD . /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
