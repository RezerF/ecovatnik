FROM ubuntu:latest
LABEL authors="pp"
RUN apt-get update -y
RUN apt-get install -y python3-pip python3.10-dev python3.10-distutils
RUN apt-get install -y build-essential
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python3.10"]
CMD ["app.py"]