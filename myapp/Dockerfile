FROM python:3
COPY . /usr/src/mimic
RUN pip install -r requirements.txt
CMD [ "python", "./webservice.py" , "-p 8000"]