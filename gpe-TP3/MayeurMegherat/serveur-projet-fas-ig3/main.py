#!/usr/bin/env python
# -*- coding: utf8 -*-
import webapp2


class Utilisateur:
    def __init__(self):
        self.latitude = None  # latitude actuelle du participant
        self.longitude = None  # longitude actuelle du participant


class Interface(webapp2.RequestHandler):
    # Initialisation des attributs de classe (statiques)
    user = Utilisateur()

    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        try:
            cmd = self.request.get('cmd')
            if cmd == 'getPosition':
                lat = self.user.latitude
                lon = self.user.longitude
                self.response.write(lat + ", " + lon)
            elif cmd == 'setPosition':
                lat = self.request.get("lat").encode()
                lon = self.request.get("lon").encode()
                self.user.latitude = lat
                self.user.longitude = lon
                self.response.write("Ok")
        except:
            self.response.write(None)


app = webapp2.WSGIApplication([
    ('/', Interface)
], debug=True)
