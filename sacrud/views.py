import deform

from pyramid.httpexceptions import HTTPFound
from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError

from .models import (
    DBSession,
    )


@view_config(context='sacrud.resources:RootResource',
             renderer='templates/catalog.mako')
def catalog(context, request):
    return {'models': context.models}

@view_config(context='sacrud.resources:ModelResource',
             renderer='templates/manage.mako')
def manage(context, request):
    return {'model': context.model}

@view_config(name='add',
             context='sacrud.resources.ModelResource',
             renderer='templates/model_add.mako')
def model_add(context, request):
    form = context.form('add')
    if 'add' in request.POST:
        controls = request.POST.items()
        print controls
        try:
            appstruct = form.validate(controls)
        except deform.ValidationFailure as e:
            return {'model': context.model,
                    'form': e.render()}
        
        obj = context.model(**appstruct)
        DBSession.add(obj)
        DBSession.flush()
        
        next_url = '/'.join(request.url.split('/')[:-1] + ['edit', str(obj.id)])
        return HTTPFound(location=next_url)
    
    return {'model': context.model,
            'form': form.render()}
