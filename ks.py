# -*- coding: utf-8 -*-
import cherrypy

class ks_site:
    @cherrypy.tools.template(name='index')
    def index(self):
        # CherryPy will call this method for the root URI ("/") and send
        # its return value to the client. Because this is tutorial
        # lesson number 01, we'll just send something really simple.
        # How about...
        return {'site_title': '12'}
