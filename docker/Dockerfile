FROM python:3.9-slim-buster

RUN pip install flask flask-sqlalchemy flask-login
RUN apt-get update && apt-get install -y sqlite3

ENV FLASK_APP=robot_deployer
WORKDIR /home
ENTRYPOINT ["flask", "run"]
