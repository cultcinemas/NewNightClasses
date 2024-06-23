FROM python:3.8-slim-buster

WORKDIR /app
RUN chmod 777 /AkEntertainmentsbot

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD ["python3", "main.py"]
