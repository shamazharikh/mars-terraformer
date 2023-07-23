FROM pytorch/pytorch:latest
RUN export DEBIAN_FRONTEND=noninteractive

RUN apt-get update 

ADD . /workspaces/

ENV PYTHONPATH /workspaces

WORKDIR /workspaces
RUN pip install -r requirements.txt
#     && apt-get -y install --no-install-recommends <your-package-list-here>
