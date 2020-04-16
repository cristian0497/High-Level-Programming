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

    st = session.query(State).first()
    if (st):
        print("{}: {}".format(st.id, st.name))
    else:
        print("Nothing")
    session.close()

if __name__ == "__main__":
    main()
