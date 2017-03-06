#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#


import os

import webapp2
import jinja2

from google.appengine.ext import ndb
from models import Form


template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir))


class Handler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str( self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)
    
    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))
        

class ResultsPageHandler(Handler):

    def get(self):
        
        first_name = self.request.get("first_name")
        last_name = self.request.get("last_name")
        country = self.request.get("country")
        children = self.request.get("children")

        propCountry = str(country).replace('+',' ').replace('_',' ').title()

        if (children == "No"):
            forms = ndb.gql("SELECT * FROM Form " + "WHERE name != 'I-730' ORDER BY name ASC")                                 

        if (children == "Yes"):
            forms = ndb.gql("SELECT * FROM Form ORDER BY name DESC")

        countryInfo = ndb.gql("SELECT * FROM Country WHERE name = :1", propCountry)
                                         
        
        if first_name and last_name and country and children:
            
            self.render('results.html', fName=first_name, lName=last_name, forms = forms, countryInfo=countryInfo)

class TranslatorPageHandler(Handler):

    def get(self):
        
        tranCountry = self.request.get("tranCountry")

        propTCountry = str(tranCountry).replace('+',' ').replace('_',' ').title()
        
        translators = ndb.gql("SELECT * FROM Translator " +
                              "WHERE country = :1 ORDER BY name DESC ", propTCountry)
        count = 1;

        if translators:            
            self.render('translators.html', translators = translators, count = count)            

         
app = webapp2.WSGIApplication([
    ('/results', ResultsPageHandler),
    ('/translators', TranslatorPageHandler)    
    ], debug=True)

