##############################
### IMPORTS                ###
##############################

from pyramid.security import Allow, Everyone
from sqlalchemy import (
    Column,
    Integer,
    Text,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from zope.sqlalchemy import ZopeTransactionExtension

##############################
### CODE                   ###
##############################

Base = declarative_base()
DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))


class Page(Base):
    __tablename__ = 'test_table'
    uid = Column(Integer, primary_key=True)
    title = Column(Text, unique=True)
    body = Column(Text)

class SomeData(Base):
    __tablename__ = 'some_data'
    uid = Column(Integer, primary_key=True)
    x_data = Column(Integer, unique=True)
    y_data = Column(Integer)

class SomeData_2(Base):
    __tablename__ = 'some_data_2'
    id = Column(Integer, primary_key=True)
    x_data = Column(Integer, unique=True)
    y_data = Column(Integer)

class Root(object):
    __acl__ = [(Allow, Everyone, 'view'),
               (Allow, 'group:editors', 'edit')]

    def __init__(self, request):
        pass

