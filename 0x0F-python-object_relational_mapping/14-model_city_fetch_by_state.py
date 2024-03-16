#!/usr/bin/python3
"""
prints all City objects from the database hbtn_0e_14_usa
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import City
import sys

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    queryResult = session.query(City, State) \
                                .join(State, City.state_id == State.id) \
                                .order_by(City.id)
    for city, state in queryResult:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
