docker run --name mongo -d mongo
docker run --name webservice -p "8000:8000" --link mongo:some-development-mongo-host -d webservice