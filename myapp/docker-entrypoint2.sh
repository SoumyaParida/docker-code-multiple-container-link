docker run --name webservice -p "8000:8000" --link mongo:mongo -d myapp/webservice