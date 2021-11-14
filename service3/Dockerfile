FROM python:3.7-slim-buster
ADD . /
WORKDIR /
RUN pip3 install --upgrade pip
RUN apt-get update 
RUN apt-get install ffmpeg libsm6 libxext6  -y
RUN apt update && pip install Flask && pip install psycopg2-binary
RUN pip3 install -r requirements.txt
COPY script.py .
COPY wait-for-it.sh .
CMD export FLASK_APP=script.py &&  flask run --host=0.0.0.0