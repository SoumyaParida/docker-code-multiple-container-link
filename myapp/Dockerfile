FROM python:3
RUN mkdir /usr/src/mimic
COPY . /usr/src/mimic/
RUN cd /usr/src/mimic/ && ls
ADD . /usr/src/mimic/
WORKDIR /usr/src/mimic/
RUN pip install bottle
RUN pip install pymongo
RUN pwd
ENV MYPATH /usr/src/mimic/myapp
ENV PORT 8000
EXPOSE 8000
CMD ["python","webservice.py"]
ENV PORT 27017
EXPOSE 27017
RUN chmod +x $MYPATH/docker-entrypoint1.sh
ENTRYPOINT $MYPATH/docker-entrypoint1.sh;  /bin/bash
RUN chmod +x $MYPATH/docker-entrypoint2.sh
ENTRYPOINT $MYPATH/docker-entrypoint2.sh; /bin/bash
