#!/usr/bin/python
from bottle import route, run, debug, default_app, response, get, post, request
import os
import random
from pymongo import MongoClient

# Configure DB params
db_name = 'slsdb'

# Configuration optional default development database host
default_host = 'some-development-mongo-host'
db_host = os.environ.get('MONGO_PORT_27017_TCP_ADDR', default_host)

@route('/')
def index():
    return """
    <p>Hello. Creating some default data everytime the page is visited.</p>
    <form action="/index" method="POST">
    A Greeting: <input type="text" name="str">
    <input type="submit">
    </form>
    """

#@route('/hello')
@route('/index', method='POST')
def do_index():
    client = MongoClient(db_host)
    db = client[db_name]
    blocks = ''
    string1 = request.forms.get('str')
    string2="hello"
    newString= string1+string2
    db.strings.insert({"string1":newString,"string2":string1})
    
    records=db.strings.find()
    for test in records:
        blocks+='"string value:"' + str(test) + '</div>'+'\n'
    #blocks += '<div style="clear:both"><a href="http://localhost:8000">Go back.</a></div>'
    return blocks


app = default_app()

#debug(True)
run(host='0.0.0.0', port=3000, reloader=True)