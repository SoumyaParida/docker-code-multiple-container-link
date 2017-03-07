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
ENV PORT 80 27017
EXPOSE 80 27017
CMD ["docker-entrypoint1.sh"]
CMD ["sh"]
WORKDIR /usr/src/mimic/myapp/
CMD [ "python", "webservice.py"]
WORKDIR /usr/src/mimic/myapp/
CMD ["docker-entrypoint2.sh"]
CMD ["sh"]
