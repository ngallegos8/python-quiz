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
        # print("Welcome to Python Quiz!")
        # player_input = input("Please select your player: ")

        # print("a) New Player")
        # print("b) Existing Player")

        # if player_input == "a":
        #         name = input("Enter name: ")
                
        #         new_player = Player(name=name)
        #         session.add(new_player)
        #         session.commit()
        #         print(f"Welcome {name}!")
        # elif



        def starter_menu():
            print("""
            # PUT CHARACTER ART -a logo-
            """)
            start_menu = [
            inquirer.List("options",
                            message = "Select one",
                            choices = ["Play", "View High Scores", "Quit"],
                            ),
            ]

            start_menu_responses = inquirer.prompt(start_menu)
            start_menu_responses_key = start_menu_responses["options"]

            if start_menu_responses_key == "Play":
                player_menu()
            elif start_menu_responses_key == "View High Scores":
                high_scores()
            elif start_menu_responses_key == "Quit":
                print("Quitter!")
                exit

        def player_menu():
            players = session.query(Player).all()
            player_menu_options = [
                inquirer.List("new",
                                message = "Are you a New or Existing Player?",
                                choices = ["New", "Existing"],
                                ),
            ]

            player_menu_responses = inquirer.prompt(player_menu_options)
            player_menu_responses_key = player_menu_responses["new"]

            if player_menu_responses_key == "New":
                create_new_player()
            if player_menu_responses_key == "Existing":
                if not players:
                    print("There are no existing players with that name")
                    player_menu()
                else:
                    returning_player()

        #Function that allows the player to input their information a after they click "new" from the previous function
        def create_new_player():
            player_name = session.query(Player.name).all()
            question = [
                inquirer.Text("name", message = "Enter your name please")
            ]
            answers = inquirer.prompt(question)
            new_player = Player(
                name = answers['name']
            )
            if new_player.name in [player[0] for player in player_name]:
                print("You're not new! Try logging in")
                returning_player()
            else:
                session.add(new_player)
                session.commit()
                returning_player()

        def returning_player():
            players = session.query(Player).all()
            question = [
                inquirer.List("update",
                            message = "Select yourself",
                            choices = [player for player in players],
                            ),
            ]
            logged_in_menu()

        # answer = inquirer.prompt(question)\
            

        def high_score():
            players = session.query(Player).all()
            all_scores = session.query(Result).all()
            all_scores1 = [(result.score, result.players.name) for result in all_scores]
            sorted_list = sorted(all_scores1, key = lambda k: k[0], reverse = True)
            if not players:
                print("There are no exsisting players")
            else:
                print(f"""
                Highest Score: {sorted_list[0][0]}  Player: {sorted_list[0][1]}
                Second Highest: {sorted_list[1][0]}  User: {sorted_list[1][1]}
                Third Highest: {sorted_list[2][0]}  User: {sorted_list[2][1]}
                """)
                return_to_start()

        def return_to_start ():
            return_start = [
                inquirer.List("return",
                            message = "Would you like to return to the Start menu?",
                            choices = ["Yes", "No"],
                            ),
            ]
            return_start_answers = inquirer.prompt(return_start)
            if return_start_answers["return"] == "Yes":
                starter_menu()
            elif return_start_answers["return"] == "No":
                print("You'll never make the high scores like that!")
                exit
             

        def logged_in_menu():    #needs to take in player thats selected?
            # print(f"Welcome {player.name}")
            start_menu = [
            inquirer.List("options",
                            message = "Select one",
                            choices = ["Take Quiz", "Edit Player", "Remove Player", "Quit"],
                            ),
            ]

            start_menu_responses = inquirer.prompt(start_menu)
            start_menu_responses_key = start_menu_responses["options"]

            if start_menu_responses_key == "Take Quiz":
                select_quiz()
            elif start_menu_responses_key == "Edit Player":
                edit_player()
            elif start_menu_responses_key == "Remove Player":
                delete_player()
            elif start_menu_responses_key == "Quit":
                print("Quitter!")
                exit

        # def select_quiz_topic():
        #     pass
            

        def select_quiz():
            start_menu = [
            inquirer.List("options",
                            message = "Select Difficulty",
                            choices = ["Easy", "Medium", "Hard", "Marilyn Vos Savant" "Quit"],
                            ),
            ]

            start_menu_responses = inquirer.prompt(start_menu)
            start_menu_responses_key = start_menu_responses["options"]

            if start_menu_responses_key == "Easy":
                easy_quiz()
            elif start_menu_responses_key == "Medium":
                medium_quiz()
            elif start_menu_responses_key == "Hard":
                hard_quiz()
            elif start_menu_responses_key == "Marilyn Vos Savant":
                marilyn_vos_savant_quiz()
            elif start_menu_responses_key == "Quit":
                print("Chicken!")
                exit

        def edit_player(selected_player):
            player_id = selected_player.id
            player = session.query(Player).filter_by(id = player_id).first()
            name = input("Enter a new name or press enter to keep current name: ")
            if name:
                    player.name = name
            session.commit()
            select_quiz()

        def delete_player(selected_player):
            player_id = selected_player.id
            player = session.query(Player).filter_by(id = player_id).first()
            start_menu = [
            inquirer.List("options",
                            message = "Are you sure you want to delete yourself?",
                            choices = ["Yes", "No, go back!"],
                            ),
            ]

            start_menu_responses = inquirer.prompt(start_menu)
            start_menu_responses_key = start_menu_responses["options"]

            if start_menu_responses_key == "Yes":
                session.delete(player)
                session.commit()
                print("You're outta here!")
                starter_menu()
            elif start_menu_responses_key == "No, go back!":
                logged_in_menu()
                
            


        def easy_quiz():
            pass
        def medium_quiz():
            pass
        def hard_quiz():
            pass
        def marilyn_vos_savant_quiz():
            pass



