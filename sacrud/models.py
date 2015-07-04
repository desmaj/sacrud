from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))

class ModelManager(object):
    
    def __init__(self):
        self._models = {}
    
    def add_model(self, model):
        self._models[model.__mapper__.class_] = model.__mapper__.class_
    
    def get_by_name(self, name):
        for klass in self._models:
            if klass.__name__ == name:
                return self._models[klass]
    
    def __iter__(self):
        return iter(self._models)
