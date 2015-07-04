from wsgiref.simple_server import make_server

import sacrud
from sacrud.demo.models import Address
from sacrud.demo.models import Base
from sacrud.demo.models import Person

import sqlalchemy as sa

if __name__ == '__main__':
    engine = sa.create_engine('sqlite:///:memory:')
    Base.metadata.create_all(bind=engine)
    
    crud = sacrud.create(engine)
    crud.add_model(Address)
    crud.add_model(Person)
    
    server = make_server('', 8888, crud)
    server.serve_forever()
