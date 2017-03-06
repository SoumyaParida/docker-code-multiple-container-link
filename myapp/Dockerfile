FROM python:3-onbuild
RUN pip install bottle
RUN pip install pymongo
EXPOSE  8000
CMD [ "python", "./webservice.py" , "-p 8000"]