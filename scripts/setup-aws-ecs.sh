#!/bin/bash

# configure
echo "Configuring cluster"
ecs-cli configure --region us-east-1 --cluster vodka-soda

# setup cloud formation template
echo "Creating cluster"
ecs-cli up --keypair vodka-soda --capability-iam --size 2 --vpc vpc-42661239 --subnets subnet-816984e6,subnet-2f465000 --instance-type t2.micro
