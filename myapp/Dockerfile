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
CMD ["docker-entrypoint1.sh"]
CMD ["sh"]
EXPOSE 3000 3000:3000
CMD [ "python", "webservice.py"]
CMD ["docker-entrypoint2.sh", "3000:3000"]
CMD ["sh"]
