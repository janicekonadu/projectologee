from google.appengine.ext import ndb

class Form(ndb.Model):

    name = ndb.StringProperty()
    officialName = ndb.StringProperty()
    pdfLink = ndb.StringProperty()
    description = ndb.StringProperty()
    mainLink = ndb.StringProperty()

class Translator(ndb.Model):

    name = ndb.StringProperty()
    language = ndb.StringProperty()
    country = ndb.StringProperty()
    telephone = ndb.StringProperty()
    cellPhone = ndb.StringProperty()
    address = ndb.StringProperty()

class Country(ndb.Model):
    name = ndb.StringProperty()
    unhcrAddresses = ndb.StringProperty()
    unhcrURL = ndb.StringProperty()
    email = ndb.StringProperty()
    telephone = ndb.StringProperty()
    flag = ndb.StringProperty()

