# -*- coding: utf-8 -*-
import cherrypy

class ks_site:
    @cherrypy.tools.template(name='index')
    def index(self):
        return {'site_title': '12'}

    @cherrypy.tools.template(name='film_review')
    def film_review(self, id=''):
        return {'site_title': id}
