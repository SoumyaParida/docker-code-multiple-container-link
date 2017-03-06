FROM python:3-onbuild
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY requirements.txt /usr/src/app/
RUN pip install -r requirements.txt
COPY . /usr/src/app
EXPOSE  8000
CMD [ "python", "./webservice.py" , "-p 8000"]