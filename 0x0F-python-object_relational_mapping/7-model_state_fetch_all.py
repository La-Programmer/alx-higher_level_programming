#!/usr/bin/python3
"""MODULE 7 FETCH ALL STATES USING SQLALCHEMY"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == '__main__':
    eng = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(eng.format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    for id, name in session.query(State.id, State.name).order_by(State.id):
        print('{}: {}'.format(id, name))
