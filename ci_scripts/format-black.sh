#!/bin/bash

# This script runs the black format check, given a docker image to run it in.
# Docker must be prebuilt!

if [ "$#" -gt 1 ];
then
    echo "Usage bash format-black.sh <optional DOCKER_IMG>"
    exit 126
elif [ "$#" -lt 1 ];
then
    black --version
    black . --check -l 79 --diff
else
    DOCKER_IMG=$1

    docker run --rm $DOCKER_IMG bash -c "black --version && black . --check -l 79 --diff"

fi
