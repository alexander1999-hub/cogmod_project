FROM ubuntu:20.04 
WORKDIR /
RUN apt update && apt install -y postgresql-client-12
COPY wait-for-it.sh .
COPY init.sql .