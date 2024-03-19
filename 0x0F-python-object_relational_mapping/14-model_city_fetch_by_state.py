#!/usr/bin/python3
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    eng = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(eng.format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    c_id = City.state_id
    id = State.id
    for city, state in session.query(City, State).filter(c_id == id).all():
        print('{}: ({}) {}'.format(state.name, city.id, city.name))
