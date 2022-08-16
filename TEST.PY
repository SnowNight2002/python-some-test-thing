#!/usr/bin/python

from flask import Flask
test = Flask(__name__)

@test.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ =="__main__":
   test.run(debug=True, port=8080)
#print ('123123')