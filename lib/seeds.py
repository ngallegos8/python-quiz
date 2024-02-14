from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

if __name__ == '__main__':
    # Create the database engine
    engine = create_engine('sqlite:///quizgame.db')

    # Drop all tables to reset
    # Player.__table__.drop(engine)
    # Quiz.__table__.drop(engine)
    # Result.__table__.drop(engine)

    # Create all tables defined in the models
    Base.metadata.create_all(engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()