#!__VENV_PYTHON__
# -*- coding: utf-8 -*-

import cherrypy
import os.path

conf = os.path.join(os.path.dirname(__file__), 'app.conf')

if __name__ == '__main__':
    cherrypy.config.update(conf)

    # Register the Jinja2 tool
    from jinja2_templating.j2tool import TemplateTool
    cherrypy.tools.template = TemplateTool()
    
    # Register the database plugin
    from data import DatabasePlugin
    DatabasePlugin(cherrypy.engine).subscribe()

    from ks import ks_site

    
    cherrypy.quickstart(ks_site(), config=conf)
