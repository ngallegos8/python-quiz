from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

if __name__ == '__main__':

    engine = create_engine('sqlite:///quizgame.db')

    # Drop all tables to reset
    # Player.__table__.drop(engine)
    # Quiz.__table__.drop(engine)
    # Result.__table__.drop(engine)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()