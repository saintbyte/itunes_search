#!/usr/bin/env python 
# -*- coding: utf-8 -*-
from flask import Flask,make_response
import json
import hashlib
import os
import sys
import urllib
from classes.itunes.request import AppleRequest
from classes.exceptions.exceptions import ItunesException,ItunesZeroResultsException,\
                                          ItunesGetProblemException

def resp_json(s,code):
    resp = make_response(s, code)
    resp.headers['Content-Type'] = 'application/json; charset=utf-8'
    return resp

def resp_404(s):
    return resp_json(s,404)

def resp_500(s):
    return resp_json(s,500)

def resp_ok(s):
    return resp_json(s,200)

app = Flask(__name__)

@app.route('/')
def main():
    return 'Main page'

@app.route('/rest/find/<first_name>/<last_name>')
def find(first_name,last_name):
    r = AppleRequest()
    try:
        data_json = r.searchArtist('{} {}'.format(first_name,last_name))
    except ItunesGetProblemException:
        return resp_500('Connection itunes problem')
    except:
        return resp_500('Internal Error')
    try:
        data_arr = json.loads(data_json)
    except:
        return resp_500('Itunes json parse problem')
    artist_full_name = ("{} {}".format(first_name,last_name)).lower()
    if (data_arr['resultCount'] == 0):
        return resp_404('Artist not found')
    for artist in data_arr['results']:
        if (artist['artistName'].lower() == artist_full_name and \
            artist['artistType'] == 'Artist'):
            try:
                s = (r.getAllAlbumsByArtistId(artist['artistId'])).strip()
            except ItunesGetProblemException:
                return resp_500('Connection itunes problem on get list albums')
            except:
                return resp_500('Internal Error on list albums')
            try:
                m = hashlib.md5()
                m.update(s)
                search_id = m.hexdigest()
                s_arr = json.loads(s)
                s_arr['search_id'] = search_id
                fh = open('search_id/{}'.format(search_id),'w')
                fh.close()
                s = json.dumps(s_arr)
            except:
                return resp_500('A not found')
            return resp_ok(s)
    return resp_404('Albums not found')

@app.route('/album/<int:id>')
def album(id):
    return 'Main page'

@app.route('/request/<int:search_result_id>')
def search_result(search_result_id):
    return 'Main page'

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=3033,debug=True)