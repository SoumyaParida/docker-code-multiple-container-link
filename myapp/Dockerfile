FROM python:3
COPY . /usr/src/mimic
RUN pip install -r /usr/src/mimic/requirements.txt
CMD [ "python", "./webservice.py" , "-p 8000"]