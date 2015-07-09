#-*- coding: utf-8 -*-
import urllib
from classes.exceptions.exceptions import ItunesException,ItunesZeroResultsException,\
                                          ItunesGetProblemException

class AppleRequest:
    endpoint='https://itunes.apple.com/'
    debug = True
    def __init__(self):
        pass

    def request(self,res):
        url = self.endpoint + res
        if self.debug:
            print url
        try:
            return urllib.urlopen(url).read()
        except:
            raise ItunesGetProblemException('Cant make request')

    def searchArtist(self,artist_name):
        res = 'search?term={}&limit=200&entity=allArtist&attribute=allArtistTerm'.format(urllib.quote(artist_name))
        return self.request(res)

    def getAllAlbumsByArtistId(self,ArtistId):
        res = 'lookup?id={}&entity=album&limit=200'.format(ArtistId)
        return self.request(res)

    def album(self,album_id):
        res = 'lookup?id={}&entity=song'.format(album_id)
        return self.request(res)
