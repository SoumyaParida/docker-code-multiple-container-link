FROM python:3-onbuild
mkdir /usr/src/app/
COPY . /usr/src/app/
RUN pip install /usr/src/app/
EXPOSE  8000
CMD [ "python", "./webservice.py" , "-p 8000"]