# Start from python image
FROM python:3.6

MAINTAINER Tom Meagher

RUN `# Update package list`         && \
     apt-get -yqq update            && \
                                       \
    `# Install development tools`   && \
     apt-get install -yqq              \
        git                            \
        nano                           \
        libproj-dev                    \
        libgdal-dev                    \
        gdal-bin                    && \
                                       \
    `# Delete cached packages`      && \
     apt-get clean

# Create dir for code
RUN mkdir /home/django
WORKDIR /home/django

# Copy over Python requirements and install
ADD requirements.txt /home/django/
RUN pip install -r requirements.txt

# Copy over remaining code
ADD . /home/django/
