FROM python:3.10-slim-buster

RUN apt-update -y && apy install awscli -y
WORKDIR /app

COPY . /app
RUN pip3 install -r requirements.txt

CMD [ "python3", "app.py" ]