import colander
import deform
import sqlalchemy as sa
from sqlalchemy import orm


node_for_type = {}
def represents(type_):
    def _adder(f):
        node_for_type[type_] = f
        return f
    return _adder

@represents(sa.Integer)
def _integer(column):
    return colander.SchemaNode(colander.Int(),
                               name=column.key)

@represents(sa.Unicode)
def _unicode(column):
    return colander.SchemaNode(colander.String(),
                               name=column.key)


def schema_node_for_column(column):
    return node_for_type[column.type.__class__](column)

class HTMLForm(deform.Form):
    
    @classmethod
    def form_for(cls, mapper, button):
        schema = colander.SchemaNode(colander.Mapping())
        for column in mapper.column_attrs:
            if len(column.columns) == 1 and column.columns[0].primary_key:
                continue
            schema.add(schema_node_for_column(column.columns[0]))
        return cls(schema, buttons=(button,))
