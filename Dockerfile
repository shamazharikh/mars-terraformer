FROM pytorch/pytorch:latest
# FROM nvcr.io/nvidia/pytorch:23.06-py3
RUN export DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y git

ADD . /app/

ENV PYTHONPATH /app

WORKDIR /app
RUN pip install -r requirements.txt
#     && apt-get -y install --no-install-recommends <your-package-list-here>
