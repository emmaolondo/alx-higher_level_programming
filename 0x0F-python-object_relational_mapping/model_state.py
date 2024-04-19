#!/usr/bin/python3
"""" Introduction to SQLAlchemy """
import sqlalchemy
# import connecting engine
from sqlalchemy import create_engine
# import database declarative clase
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, MetaData


meta = MetaData()
Base = declarative_base(metadata=meta)


class State(Base):
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

    def __repr__(self):
        return self.name
