FROM ubuntu:latest

COPY . /app
WORKDIR /app

RUN apt update && apt upgrade
RUN apt install -y python3
RUN apt install -y python3-pip
RUN apt install -y exiftool
RUN apt install -y binwalk
RUN apt install -y ruby
RUN gem install zsteg
RUN pip install -r requirements.txt --break-system-packages

EXPOSE 5000

# CMD ["gunicorn", "--workers", "3", "--bind", "0.0.0.0:5000", "wsgi:app"]
