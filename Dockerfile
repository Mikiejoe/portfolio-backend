FROM python:3.12

ENV PYTHONUNBUFFERED 1 
RUN mkdir /code
WORKDIR /code
ADD . /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN mkdir static
# RUN python manage.py collectstatic --no-input
EXPOSE 5000
CMD ["gunicorn","--bind", ":5000", "core.wsgi:application"]