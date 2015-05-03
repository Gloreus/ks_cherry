import postgresql

import cherrypy
from cherrypy.process import wspbus, plugins

class DatabasePlugin(plugins.SimplePlugin):
    def __init__(self, bus):
        plugins.SimplePlugin.__init__(self, bus)
        self.db = None 

    def start(self):
        self.bus.log('Starting up DB access')
        self.bus.subscribe("get_data", self.get_data)

    def stop(self):
        self.bus.log('Stopping down DB access')
        if self.db:
            self.db.close()
        self.bus.unsubscribe("get_data", self.get_data)
    
    def reconnect(self):
        self.bus.log('Reconnect..')
        self.db = None
        try:
          self.db = postgresql.open(
                      user = 'slava'
                    , host = 'localhost'
                    , port = 5432
                    , password = 'c300g'
                    , database = 'ks'
                    , connect_timeout= 100
                    )
        except Exception as e: 
            self.bus.log('Connection error:', e)
        
    def get_data(self, sql):
        if not self.db:
            self.reconnect()
            
        self.bus.log('get_data: ' + sql)
        try:
            res = self.db.prepare(sql)
        except Exception as e: 
            res = None
            self.reconnect()
        return res




