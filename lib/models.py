import inquirer
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
    alt_answers = Column(String, nullable=True)
    player_id = Column(Integer, ForeignKey("players.id"))

    players = relationship("Player", back_populates="quizzes") #DO I NEED secondary="results", for point to the association table?
    # results = relationship("Result", secondary="quizzes", back_populates="quizzes")


class Result(Base):
    __tablename__ = 'results'
    id = Column(Integer, primary_key=True)
    player_id = Column(Integer, ForeignKey("players.id"))
    quiz_id = Column(Integer, ForeignKey("quizzes.id"))
    score = Column(Integer)


