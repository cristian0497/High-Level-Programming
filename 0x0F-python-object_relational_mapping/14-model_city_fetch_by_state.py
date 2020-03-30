#!/usr/bin/python3
""" All objects """
from sys import argv
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_city import City
from model_state import State, Base


def main():
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State.name, City.id, City.name)\
                   .join(City, City.state_id == State.id)\
                   .order_by(City.id)
    for var in query.all():
        print("{}: ({}) {}".format(var.name, var.id, var.name))

    session.close()

if __name__ == "__main__":
    main()
