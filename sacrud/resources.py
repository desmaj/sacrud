from sqlalchemy import orm

from .forms import HTMLForm

class RootResource(object):
    
    @classmethod
    def factory(cls, models):
        def _root_factory(request):
            return cls(request, models)
        return _root_factory
    
    def __init__(self, request, models):
        self._request = request
        self.models = models
    
    def __getitem__(self, key):
        if key == 'manage':
            return ModelManagementResource(self._request, self.models)
        raise KeyError(key)
    

class ModelManagementResource(object):
    
    def __init__(self, request, models):
        self._request = request
        self.models = models
    
    def __getitem__(self, key):
        model = self.models.get_by_name(key)
        if model:
            return ModelResource(self._request, model)
        raise KeyError(key)


class ModelResource(object):
    
    def __init__(self, request, model):
        self._request = request
        self.model = model
    
    def form(self, action):
        mapper = orm.class_mapper(self.model)
        return HTMLForm.form_for(mapper, action)
#         for column in mapper.column_attrs:
#             print field_for_type(column.columns[0].type)
#         return fields
