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
WORKDIR /usr/src/mimic/myapp/
RUN pwd
RUN cd /usr/src/mimic/myapp/ && ls
CMD ["docker-entrypoint1.sh"]
CMD ["sh"]
CMD [ "python", "webservice.py", "-p 8000"]
RUN ls
CMD ["docker-entrypoint2.sh", "-p 8000:8000"]
CMD ["sh"]