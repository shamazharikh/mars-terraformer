#!/bin/bash
USER_NAME=`cat ./user_variables/user_name`
USER_EMAIL=`cat ./user_variables/user_email`
echo $USER_NAME
echo $USER_EMAIL
git config --global user.email $USER_EMAIL
git config --global user.name $USER_NAME
