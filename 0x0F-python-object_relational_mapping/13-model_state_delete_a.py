#!/usr/bin/python3
""" Method to print all matches with at least one A """
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

    for obj in session.query(State).filter(State.name.like('%a%')).all():
        session.delete(obj)
    session.commit()
    session.close()

if __name__ == "__main__":
    main()
