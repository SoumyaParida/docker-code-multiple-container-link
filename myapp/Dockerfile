FROM python:3
RUN mkdir /usr/src/mimic
COPY . /usr/src/mimic/
RUN cd /usr/src/mimic/ && ls
ADD . /usr/src/mimic/
WORKDIR /usr/src/mimic/
RUN pip install bottle
RUN pip install pymongo
RUN pwd
EXPOSE 8000
ENTRYPOINT ["--name mongo -d mongo"]
CMD [ "python", "myapp/webservice.py", "-p 8000"]
ENTRYPOINT ["--name webservice --link mongo:mongo -d myapp/webservice"]