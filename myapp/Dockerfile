FROM python:3-onbuild
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
EXPOSE  8000
CMD [ "python", "./webservice.py" , "-p 8000"]