FROM pytorch/pytorch:latest
RUN export DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y git

ADD . /workspaces/

ENV PYTHONPATH /workspaces

WORKDIR /workspaces
RUN pip install -r requirements.txt
#     && apt-get -y install --no-install-recommends <your-package-list-here>
