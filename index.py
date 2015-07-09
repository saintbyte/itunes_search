#!/usr/bin/env python 
# -*- coding: utf-8 -*-
from flask import Flask
import json
import os
import sys
import urllib

app = Flask(__name__)

@app.route('/')
def main():
    return 'Main page'

@app.route('/rest/find/<first_name>/<last_name>')
def find(first_name,last_name):
    return 'Main page'

@app.route('/album/<int:id>')
def album(id):
    return 'Main page'

@app.route('/request/<int:search_result_id>')
def search_result(search_result_id):
    return 'Main page'

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=3033,debug=True)