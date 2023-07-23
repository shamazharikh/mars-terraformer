FROM nvcr.io/nvidia/pytorch:23.06-py3
RUN export DEBIAN_FRONTEND=noninteractive

RUN apt-get update 

WORKDIR /workspaces
ADD requirements.txt /workspaces/
RUN pip install -r requirements.txt
#     && apt-get -y install --no-install-recommends <your-package-list-here>