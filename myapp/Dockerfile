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
ENTRYPOINT ["myapp/docker-entrypoint1.sh"]
CMD ["sh"]
CMD [ "python", "myapp/webservice.py", "-p 8000"]
ENTRYPOINT ["myapp/docker-entrypoint2.sh"]
CMD ["sh"]