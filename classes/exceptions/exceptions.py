#-*- coding: utf-8 -*-
class MyBaseException(Exception):
   def __init__(self, value):
       self.value = value
   def __str__(self):
       return repr(self.value)

class ItunesException(MyBaseException):
    pass

class ItunesZeroResultsException(MyBaseException):
    pass

class ItunesGetProblemException(MyBaseException):
    pass