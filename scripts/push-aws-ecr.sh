#!/bin/bash

# build containers
echo "Building containers"
docker build -t api ./api
docker build -t web ./web
docker build -t nginx ./nginx

# tag containers
echo "Tagging containers"
docker tag api:latest 102953801091.dkr.ecr.us-east-1.amazonaws.com/api:latest
docker tag web:latest 102953801091.dkr.ecr.us-east-1.amazonaws.com/web:latest
docker tag nginx:latest 102953801091.dkr.ecr.us-east-1.amazonaws.com/nginx:latest

# Login to AWS ECR
$(aws ecr get-login --region us-east-1)

# push containers
echo "Pushing containers"
docker push 102953801091.dkr.ecr.us-east-1.amazonaws.com/api:latest
docker push 102953801091.dkr.ecr.us-east-1.amazonaws.com/web:latest
docker push 102953801091.dkr.ecr.us-east-1.amazonaws.com/nginx:latest
