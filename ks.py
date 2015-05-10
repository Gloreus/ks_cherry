# -*- coding: utf-8 -*-
import cherrypy

class ks_site:
    @cherrypy.tools.template(name='index')
    def index(self):
        return {'site_title': '12'}

    @cherrypy.tools.template(name='film_review')
    def film_review(self, id=''):
        res = cherrypy.engine.publish("get_data", 'select 1').pop()
        if res:
            s = res.first()
        else:
            s = 'error'     
        return {'site_title': s}

    @cherrypy.tools.template(name='ed_film')
    def new_film(self):
        return {'site_title': '12', 'page_title': 'Карточка фильма'}
