#!/bin/bash

# update environment variables
echo "Updating environment variables"
source .env

# accept user input
echo "Enter superuser info"
read -p "Username: " username
read -p "Email: " email
read -sp "Password: " password
read -sp "Confirm password: " confirmPassword

if [ ${#password} -ge 5 ] && [ $password == $confirmPassword ]; then
    echo "Creating superuser"
    ecs-cli compose --file aws-compose.yml run api "python manage.py createsu $username $email $password"
else
    echo "Passwords do not match :("
fi
