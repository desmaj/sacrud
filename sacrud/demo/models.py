import sqlalchemy as sa

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Person(Base):
    __tablename__ = 'persons'
    
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.Unicode(255))

class Address(Base):
    __tablename__ = 'addresses'
    
    id = sa.Column(sa.Integer, primary_key=True)
    street = sa.Unicode(1023)
    city = sa.Unicode(255)
    state = sa.Unicode(255)
    person_id = sa.Column(sa.Integer, sa.ForeignKey(Person.id))
    
    person = sa.orm.relationship(Person, uselist=False, backref='addresses')
    
    def __repr__(self):
        return '{} {}, {}'.format(self.street, self.city, self.state)

                 
