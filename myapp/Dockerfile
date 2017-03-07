FROM python:3
RUN mkdir /usr/src/mimic
COPY . /usr/src/mimic/
RUN cd /usr/src/mimic/ && ls
ADD . /usr/src/mimic/
WORKDIR /usr/src/mimic/
RUN pip install bottle
RUN pip install pymongo
RUN pwd
WORKDIR /usr/src/mimic/myapp/
EXPOSE 8000
CMD ["docker-entrypoint1.sh"]
CMD ["sh"]
CMD [ "python", "webservice.py"]
CMD ["docker-entrypoint2.sh", "8000"]
CMD ["sh"]