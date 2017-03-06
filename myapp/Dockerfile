FROM python:3-onbuild 
COPY . /usr/src/app
RUN pip install -r requirements.txt
EXPOSE  8000
CMD [ "python", "./webservice.py" , "-p 8000"]