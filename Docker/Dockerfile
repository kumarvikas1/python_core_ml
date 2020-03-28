FROM python:3

WORKDIR /opt/

COPY ./requirements.txt ./
COPY ./setup.py ./
RUN pip install -r requirements.txt

ADD /dist/controller-1.0-py3.7.egg /opt/egg/controller.egg