#!/usr/bin/env python
from classes.itunes.request import AppleRequest
from classes.exceptions.exceptions import ItunesException,ItunesZeroResultsException,\
                                          ItunesGetProblemException
import simplejson as json
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

def getArtistSearch(first_name,last_name):
    r = AppleRequest()
    try:
        data_json = r.searchArtist('{} {}'.format(first_name,last_name))
    except ItunesGetProblemException: 
        return 0
    except:
        return 0

    data_arr = json.loads(data_json)

    artist_full_name = ("{} {}".format(first_name,last_name)).lower()
    if (data_arr['resultCount'] == 0):
         return 0
    for artist in data_arr['results']:
        if (artist['artistName'].lower() == artist_full_name and \
            artist['artistType'] == 'Artist'):
            r.getAllAlbumsByArtistId(artist['artistId'])
            return artist['artistId']
    """
        print "{}|{}|{}|{}".format(artist['artistName'].lower(),artist['artistType'],
                               artist['artistId'],'')
    """

lenon_id =  getArtistSearch('John','Lennon')
r.getAllAlbumsByArtistId
print "--------------------------"
print getArtistSearch('jack','johnson')
print "--------------------------"
print getArtistSearch('Kirkorov','Vasya')


#print data_arr