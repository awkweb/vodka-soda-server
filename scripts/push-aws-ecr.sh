#!/bin/bash

# build containers
docker build -t django ./django
docker build -t nginx ./nginx

# tag containers
docker tag django:latest 102953801091.dkr.ecr.us-east-1.amazonaws.com/django:latest
docker tag nginx:latest 102953801091.dkr.ecr.us-east-1.amazonaws.com/nginx:latest

# push containers
docker push 102953801091.dkr.ecr.us-east-1.amazonaws.com/django:latest
docker push 102953801091.dkr.ecr.us-east-1.amazonaws.com/nginx:latest
