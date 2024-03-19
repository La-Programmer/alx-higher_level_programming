#!/usr/bin/python3
"""MODULE 10 FETCH THE ROW WITH A USER INPUTTED NAME USING SQLALCHEMY"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == '__main__':
    eng = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(eng.format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    name = sys.argv[4]
    res = session.query(State).filter(State.name.in_([name])).first()
    if (res):
        print(res.id)
    else:
        print('Not found')
