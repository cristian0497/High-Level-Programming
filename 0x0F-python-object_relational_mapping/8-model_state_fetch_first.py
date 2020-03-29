#!/usr/bin/python3
""" Print all objects in sql with alchemy"""
from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def main():
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    st = session.query(State).order_by(State.id).all()
    if (len(st) > 0):
        print("{}: {}".format(st[0].id, st[0].name))
    else:
        print("Nothing")

    session.close()

if __name__ == "__main__":
    main()
