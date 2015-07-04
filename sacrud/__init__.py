from pyramid.config import Configurator

from .application import CRUDApplication
from .models import DBSession
from .models import ModelManager
from .resources import RootResource

def create(engine):
    """ This function returns a Pyramid WSGI application.
    """
    DBSession.configure(bind=engine)
    models = ModelManager()
    config = Configurator(root_factory=RootResource.factory(models))
    config.include('pyramid_mako')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.scan()
    app =  config.make_wsgi_app()
    return CRUDApplication(app, engine, models)
