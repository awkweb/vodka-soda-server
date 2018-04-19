# Start from python image
FROM python:3.6

MAINTAINER Tom Meagher

# Create dir for code
RUN mkdir /home/web
WORKDIR /home/web

# Copy over Python requirements and install
ADD requirements.txt /home/web/
RUN pip install -r requirements.txt

# Copy over remaining code
ADD . /home/web/

VOLUME /home/web
