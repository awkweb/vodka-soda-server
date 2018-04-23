#!/bin/bash

# substitute nginx env variables
bash -c "envsubst < /etc/nginx/nginx.tmpl > /etc/nginx/nginx.conf && nginx -g 'daemon off;'"
