FROM python:3.10-alpine

LABEL version=1.0

RUN mkdir -p home/app

COPY . /app

RUN pip install -r app/requirements.txt

CMD python /app/app.py
