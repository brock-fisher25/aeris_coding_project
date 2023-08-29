FROM ubuntu:22.04
RUN apt-get update
RUN apt-get install pip -y
RUN apt-get install python3-dev
RUN pip install --upgrade pip
WORKDIR /app
COPY . /app
RUN pip --no-cache-dir install -r requirements.txt
WORKDIR /app/flask
CMD ["python3", "app.py"]