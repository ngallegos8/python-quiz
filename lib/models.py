from sqlalchemy import create_engine, ForeignKey, Column, Integer, String
from sqlalchemy.orm import sessionmaker, relationship, validates, declarative_base

Base = declarative_base()

# Player has many quizzes(questions), a quiz(question) has many results(each time taken)...player has many results

class Player(Base):
    __tablename__ = "players"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    times_played = Column(Integer, nullable=True)
    avg_score = Column(Integer, nullable=True)
    high_score = Column(Integer, nullable=True)
    quizzes = relationship("Quiz", back_populates="players") #DO I NEED secondary="results", for point to the association table?

    #create a validation
    @validates("name")
    def validate_name(self, key , name):
            if not name:
                    raise ValueError("Name cannot be empty")
            else:
                    return name
            
    #create a repr
    def __repr__(self):
        return f"{self.name}"
    

class Quiz(Base):
    __tablename__ = 'quizzes'
    id = Column(Integer, primary_key=True)
    question_text = Column(String, nullable=False)
    correct_answer = Column(String, nullable=False)
    alt_answers = Column(String, nullbale=True)

    players = relationship("Player", back_populates="quizzes") #DO I NEED secondary="results", for point to the association table?
    # results = relationship("Result", secondary="quizzes", back_populates="quizzes")


class Result(Base):
    __tablename__ = 'results'
    id = Column(Integer, primary_key=True)
    player_id = Column(Integer, ForeignKey("players.id"))
    quiz_id = Column(Integer, ForeignKey("quizzes.id"))
    score = Column(Integer)


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

    while True:
        print("Welcome to Quiz!")
        print("a) New User")
        print("b) Existing user")

        user_input = input("Select your user : ")

        if user_input == "a":
                name = input("Enter name: ")
                elevation = input("Enter elevation: ")
                location = input("Enter a location: ")

                try: 
                    elevation = int(elevation)
                except ValueError:
                    print("Invalid input, must be a number")
                    continue
                
                new_mountain = Mountain(name=name, elevation=elevation, location=location)
                session.add(new_mountain)
                session
                session.commit()
                print("Added!")
