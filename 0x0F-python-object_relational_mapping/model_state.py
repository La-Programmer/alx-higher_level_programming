#!/usr/bin/python3
"""MODULE 6 THE BEGINNING OF USING SQLALCHEMY"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
