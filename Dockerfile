# start from base
FROM ubuntu:latest

# install system-wide deps for python and node
RUN apt-get -yqq update
RUN apt-get -yqq install python-pip python-dev

# copy our application code
ADD . /opt/rubic_cube
WORKDIR /opt/rubic_cube

RUN pip install -r requirements.txt

# start app
CMD [ "python", "./main.py" ]
