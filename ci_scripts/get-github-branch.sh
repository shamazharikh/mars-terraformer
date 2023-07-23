#!/bin/bash
#Obtains branch name from GitHub environment variables for github actions

branch=${GITHUB_HEAD_REF#refs/heads/}
if [ -z "$branch" ];
then
    branch=${GITHUB_REF#refs/heads/}
fi

echo $branch
