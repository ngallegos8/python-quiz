import random
import inquirer
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Player, Quiz, Result
from easy_quiz import *
from medium_quiz import *
from hard_quiz import *
from marilyn_vos_savant_quiz import *


# def create_session():
if __name__ == '__main__':
    engine = create_engine('sqlite:///quizgame.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    # return session



# # tied to the questions table in models.py to perfom full CRUD on the 'questions' table 
# def seed_questions_and_results(name):
#     session = create_session()

# QUESTIONS = {
#     "Which one of the following rhythm games was made by Harmonix?": [
#         "Rock Band", "Meat Beat Mania", "Guitar Hero Live", "Dance Dance Revolution"
#     ],
#     "What machine element is located in the center of fidget spinners?": [
#         "Bearings", "Axles", "Gears", "Belts"
#     ],
#     "Which American-owned brewery led the country in sales by volume in 2015?": [
#         "D. G. Yuengling and Son, Inc", "Anheuser Busch", "Boston Beer Company", "Miller Coors"
#     ],
#     "What is Tasmania?": [
#         "An Australian State", "A flavor of Ben and Jerry's ice-cream", "A Psychological Disorder", "The Name of a Warner Brothers Cartoon Character"
#     ],
#     "What is the Zodiac symbol for Gemini?": [
#       "Twins", "Fish", "Scales", "Maiden"
#     ],
#     "When one is 'envious', they are said to be what color?": [
#         "Green", "Red", "Blue", "Yellow"
#     ],
#     "Who invented the first ever chocolate bar, in 1847?": [
#         "Joseph Fry", "Andrew Johnson", "John Cadbury", "John Tyler"
#     ],
#     "Which of these colours is NOT featured in the logo for Google?": [
#         "Pink", "Yellow", "Blue", "Green"
#     ],
#     "How would one say goodbye in Spanish?": [
#         "Adiós","Hola", "Au Revoir", "Salír"
#     ],
#     "In the video-game franchise Kingdom Hearts, the main protagonist, carries a weapon with what shape?": [
#         "Key", "Sword", "Pen", "Cellphone"
#     ]
# }

# for question, alternatives in QUESTIONS.items():
#     correct_answer = alternatives[0]
#     sorted_alternatives = sorted(alternatives)
#     for label, alternative in enumerate(sorted_alternatives):
#         print(f"  {label}) {alternative}")

#     answer_label = int(input(f"{question}? "))
#     answer = sorted_alternatives[answer_label]
#     if answer == correct_answer:
#         print("Correct!")
#     else:
#         print(f"The answer is {correct_answer!r}, not {answer!r}")

# # in this function, there is CRUD happening to the quizzes table 
# if __name__ == '__main__':
#     # Create the database engine
#     engine = create_engine('sqlite:///quizgame.db')

#     # Drop all tables to reset
#     # Player.__table__.drop(engine)
#     # Quiz.__table__.drop(engine)
#     # Result.__table__.drop(engine)

#     # Create all tables defined in the models
#     Base.metadata.create_all(engine)

#     # Create a session
#     Session = sessionmaker(bind=engine)
#     session = Session()

#     while True:
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
            player_menu()
        else:
            session.add(new_player)
            session.commit()
            returning_player()


    # def returning_player():
    #     players = session.query(Player).all()
    #     returning_player_options = [
    #         inquirer.List("choose",
    #                       message = "Select Yourself",
    #                       choices =[player for player in players])
    #     ]
    #     # print(players)
    #     answer = inquirer.prompt(returning_player_options)
    #     answer_key = answer["choose"]
    #     player_choice = answer_key.id

    #     def player_obj():
    #         if player_choice == Player.name in players:
    #             return Player.id
            

    #     selected_player = player_obj
    #     logged_in_menu(selected_player)



    def returning_player():
        players = session.query(Player).all()
        returning_player_options = [
            inquirer.List("choose",
                          message = "Select Yourself",
                          choices =[player for player in players])
        ]
        # print(players)
        answer = inquirer.prompt(returning_player_options)
        answer_key = answer["choose"]
        print(answer_key)
        player = answer_key.id
        print(type(player))
        selected_player = player
        logged_in_menu(selected_player)

        

    def high_scores():
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
        

    def logged_in_menu(selected_player):    #needs to take in player thats selected?
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
            select_quiz(selected_player)
        elif start_menu_responses_key == "Edit Player":
            edit_player(selected_player)
        elif start_menu_responses_key == "Remove Player":
            delete_player(selected_player)
        elif start_menu_responses_key == "Quit":
            print("Quitter!")
            exit

    # def select_quiz_topic():
    #     pass
            

    def select_quiz(selected_player):
        # quizzes = session.query(Quiz).all()

        select_quiz_options = [
        inquirer.List("choose",
                        message = "Select Difficulty",
                        choices = ["Easy", "Medium", "Hard", "Marilyn Vos Savant", "Quit"]
                        ),
        ]

        answer = inquirer.prompt(select_quiz_options)
        answer_key = answer["choose"]
        print(answer)
        # quiz = answer_key.id
        # selected_quiz = quiz

        if answer_key == "Easy":
            new_easy_quiz = Quiz(name="Easy", player_id=selected_player)
            session.add(new_easy_quiz)
            session.commit()
            easy_quiz(selected_player, new_easy_quiz)
        elif answer_key == "Medium":
            medium_quiz(selected_player)
        elif answer_key == "Hard":
            hard_quiz(selected_player)
        elif answer_key == "Marilyn Vos Savant":
            marilyn_vos_savant_quiz(selected_player)
        elif answer_key == "Quit":
            print("Chicken!")
            exit



        

    # def select_quiz(selected_player):
    #     select_quiz_options = [
    #     inquirer.List("choose",
    #                     message = "Select Difficulty",
    #                     choices = ["Easy", "Medium", "Hard", "Marilyn Vos Savant", "Quit"]
    #                     ),
    #     ]

    #     answer = inquirer.prompt(select_quiz_options)
    #     answer_key = answer["choose"]
    #     quiz = answer_key.id
    #     selected_quiz = quiz

    #     if answer_key == "Easy":
    #         new_easy_quiz = Quiz(name="Easy", player_id=selected_player)
    #         session.add(new_easy_quiz)
    #         session.commit()
    #         easy_quiz(selected_player, new_easy_quiz)
    #     elif answer_key == "Medium":
    #         medium_quiz(selected_player)
    #     elif answer_key == "Hard":
    #         hard_quiz(selected_player)
    #     elif answer_key == "Marilyn Vos Savant":
    #         marilyn_vos_savant_quiz(selected_player)
    #     elif answer_key == "Quit":
    #         print("Chicken!")
    #         exit



    # def returning_player():
    #     players = session.query(Player).all()
    #     returning_player_options = [
    #         inquirer.List("choose",
    #                       message = "Select Yourself",
    #                       choices =[player for player in players])
    #     ]
    #     answer = inquirer.prompt(returning_player_options)
    #     answer_key = answer["choose"]
    #     player = answer_key.id
    #     selected_player = player
    #     logged_in_menu(selected_player)



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
            
        


    def easy_quiz(selected_player, new_easy_quiz):
        
        print(new_easy_quiz)
        print(selected_player)
        # run_easy_quiz()
        score = run_easy_quiz()
        result = Result(player_id=selected_player, quiz_id=new_easy_quiz.id, score=score)
        session.add(result)
        session.commit()
    def medium_quiz():
        run_medium_quiz()
    def hard_quiz():
        run_hard_quiz()
    def marilyn_vos_savant_quiz():
        run_marilyn_vos_savant_quiz()

    starter_menu()




