#!/usr/bin/python3
"""MODULE 12 CHANGE ROW NAME BASED ON ID USING SQLALCHEMY"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == '__main__':
    eng = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(eng.format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    res = session.query(State).filter(State.id == 2).first()
    res.name = 'New Mexico'
    session.commit()
