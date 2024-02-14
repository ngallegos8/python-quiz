from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

# in this function, there is CRUD happening to the quizzes table 
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

    # # Fetch the existing questions from the database
    # questions = session.query(Quiz).all()
    # question_texts = set(question.question_text for question in questions)

    # results = session.query(Result).all()
    # results_after = 

    # session.commit()

    # # Close the session when you're done
    # session.close()

    

    







# if __name__ == "__main__":
#     engine = create_engine("sqlite:///game.db")
#     # Player.__table__.drop(engine)
#     # Quiz.__table__.drop(engine)
#     # Result.__table__.drop(engine)
#     Base.metadata.create_all(engine)

#     with Session(engine) as session:
#         fake = Faker()

#         for _ in range(10):
#             teacher = Teacher(name = fake.name(), subject = fake.word())
#             session.add(teacher)

#         for _ in range(20):
#             student = Student(name = fake.name(), email = fake.email(), emergency_email = fake.email(), teacher_id = fake.random_int(min=1, max=10))
#             session.add(student)

#         session.commit()

#         # NOT NECESSARY BUT CAN ADD
#         session.close()