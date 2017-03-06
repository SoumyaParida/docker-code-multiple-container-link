FROM python:3
COPY . /usr/src/mimic
ADD . /usr/src/mimic
WORKDIR /usr/src/mimic
RUN pip install bottle
RUN pip install pymongo
CMD [ "python", "webservice.py"]