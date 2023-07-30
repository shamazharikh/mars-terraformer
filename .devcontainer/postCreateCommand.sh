#!/bin/bash
if [ -s /user_variables/user_email ]; then
    USER_NAME=`cat ./user_variables/user_name`
    USER_EMAIL=`cat ./user_variables/user_email`
else
    USER_NAME="Mazhar Shaikh"
    USER_EMAIL="mazharshaikh94@gmail.com"
fi
echo $USER_NAME
echo $USER_EMAIL
git config --global user.email $USER_EMAIL
git config --global user.name $USER_NAME
