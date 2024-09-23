FROM python:3.12

ENV PYTHONUNBUFFERED 1 
RUN mkdir /code
WORKDIR /code
ADD . /code/
ARG CLOUD_NAME
ARG API_KEY
ARG API_SECRET 
ARG DB_NAME
ARG DB_PASSWORD
ARG DB_HOST
ARG DB_PORT
ARG EMAIL_HOST_USER
ARG EMAIL_HOST_PASSWORD
ARG EMAIL_PORT
ARG EMAIL_HOST


RUN pip install --upgrade pip
RUN pip install -r requirements.txt
# RUN mkdir static
# RUN python manage.py collectstatic --no-input
EXPOSE 5000
CMD ["gunicorn","--bind", ":5000", "cms.wsgi:application"]