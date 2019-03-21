# Start from python image
FROM python:3.6

# Create dir for code
RUN mkdir /home/api
WORKDIR /home/api

# Copy over Python requirements and install
ADD requirements.txt /home/api/
RUN pip install -r requirements.txt

# Copy over remaining code
ADD . /home/api/
VOLUME /home/api
