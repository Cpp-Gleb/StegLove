FROM ubuntu:latest

COPY . /app
WORKDIR /app

ARG DEBIAN_FRONTEND=noninteractive

RUN apt update -y && apt upgrade -y
RUN apt install -y python3
RUN apt install -y python3-pip
RUN apt install -y exiftool
RUN apt install -y binwalk
RUN apt install -y ruby
RUN apt install -y ghc
RUN gem install zsteg
RUN pip install -r requirements.txt --break-system-packages

RUN cd /app && ghc -o core/uuid-generator/uuid-list-exe core/uuid-generator/myuuid.hs core/uuid-generator/src/FeistelPermutation.hs core/uuid-generator/src/UUIDList.hs && chmod +x core/uuid-generator/uuid-list-exe

EXPOSE 5000

# CMD ["gunicorn", "--workers", "3", "--bind", "0.0.0.0:5000", "wsgi:app"]
