FROM python:3.10-alpine
LABEL version=1.0
RUN mkdir -p home/app
WORKDIR /app
COPY . /app
RUN chown -R $USER:$USER /app
RUN chmod 777 /app
RUN pip install -r requirements.txt
CMD python app.py

#docker run -d -p 8081:8081 -v main_volume:/home/app/database --name sintia_app sintia
