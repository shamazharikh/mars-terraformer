FROM nvcr.io/nvidia/pytorch:23.06-py3
RUN export DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y git

ADD . /app
ENV PYTHONPATH /app

WORKDIR /app
ADD ./requirements.txt .
RUN pip install -r requirements.txt


