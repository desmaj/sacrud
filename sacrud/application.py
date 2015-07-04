from .models import ModelManager

class CRUDApplication(object):
    
    def __init__(self, wsgiapp, engine, manager):
        self._wsgiapp = wsgiapp
        self._engine = engine
        self._manager = manager
    
    def add_model(self, mapped_klass):
        self._manager.add_model(mapped_klass)
    
    def __call__(self, environ, start_response):
        return self._wsgiapp(environ, start_response)
