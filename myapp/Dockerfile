FROM python:3
COPY . /usr/src/mimic
RUN pip install bottle
RUN pip install pymongo
CMD [ "python", "/usr/src/mimic/webservice.py" , "-p 8000"]