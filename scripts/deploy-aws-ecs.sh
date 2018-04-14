#!/bin/bash

# update environment variables
echo "Updating environment variables"
source .env

# deploy
echo "Deploying to ECS"
ecs-cli compose --file aws-compose.yml up

# check
echo "Running containers"
ecs-cli ps
