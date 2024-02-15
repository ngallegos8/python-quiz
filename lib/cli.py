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


    def starter_menu():
        print("""
\u001B[2m\u001B[36m---------------------------------------------------------------------------------------------------\u001B[2m\u001B[0m 
\u001B[3m\u001B[96m              
█▀▀█ 　 █▀▀█ █──█ ▀▀█▀▀ █──█ █▀▀█ █▀▀▄ 　 █▀▀█ █──█ ─▀─ ▀▀█ 　 █▀▀█ █▀▀█ █▀▀█ 　 ▀▀█▀▀ █▀▀█ 　 █▀▀ ─▀─ █▀▀▄ █▀▀▄ 
█▄▄█ 　 █──█ █▄▄█ ──█── █▀▀█ █──█ █──█ 　 █──█ █──█ ▀█▀ ▄▀─ 　 █▄▄█ █──█ █──█ 　 ──█── █──█ 　 █▀▀ ▀█▀ █──█ █──█ 
▀──▀ 　 █▀▀▀ ▄▄▄█ ──▀── ▀──▀ ▀▀▀▀ ▀──▀ 　 ▀▀▀█ ─▀▀▀ ▀▀▀ ▀▀▀ 　 ▀──▀ █▀▀▀ █▀▀▀ 　 ──▀── ▀▀▀▀ 　 ▀── ▀▀▀ ▀──▀ ▀▀▀─ 

█▀▀█ █──█ ▀▀█▀▀ 
█──█ █──█ ──█── 
▀▀▀▀ ─▀▀▀ ──▀──... \u001B[3m\u001B[0m
                                 
\u001B[1m\u001B[36m
█▀▀█ █▀▄▀█ 　 ░▀░ 　 ▒█▀▀▀█ █▀▄▀█ █▀▀█ █▀▀█ █▀▀█ ▀▀█▀▀ ▀█ 
█▄▄█ █░▀░█ 　 ▀█▀ 　 ░▀▀▀▄▄ █░▀░█ █▄▄█ █▄▄▀ █▄▄▀ ░░█░░ █▀ 
▀░░▀ ▀░░░▀ 　 ▀▀▀ 　 ▒█▄▄▄█ ▀░░░▀ ▀░░▀ ▀░▀▀ ▀░▀▀ ░░▀░░ ▄░\u001B[1m\u001B[0m
              
\u001B[2m\u001B[36m---------------------------------------------------------------------------------------------------\u001B[2m\u001B[0m                                                                                    
              
        """)
        start_menu = [
        inquirer.List("options",
                        message = "\x1b[35;3mWelcome! Please select\x1b[35;0m",
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
            print("\x1b[35;3mQuitter!\x1b[35;0m")
            exit

    def player_menu():
        print("\u001B[2m\u001B[36m---------------------------------------------------------------------------------------------------\u001B[2m\u001B[0m \n ")
        players = session.query(Player).all()
        player_menu_options = [
            inquirer.List("new",
                            message = "\x1b[35;3mAre you a New or Existing Player?\x1b[35;0m",
                            choices = ["New", "Existing", "Go Back to Main Menu"],
                            ),
        ]

        player_menu_responses = inquirer.prompt(player_menu_options)
        player_menu_responses_key = player_menu_responses["new"]

        if player_menu_responses_key == "New":
            create_new_player()
        if player_menu_responses_key == "Existing":
            if not players:
                print("\x1b[35;3mThere are no existing players with that name\x1b[35;0m")
                player_menu()
            else:
                returning_player()
        elif player_menu_responses_key == "Go Back to Main Menu":
            starter_menu()


    def create_new_player():
        print("\u001B[2m\u001B[36m---------------------------------------------------------------------------------------------------\u001B[2m\u001B[0m \n ")
        player_name = session.query(Player.name).all()
        question = [
            inquirer.Text("name", message = "\x1b[35;3mEnter your name please\x1b[35;0m")
        ]

        answers = inquirer.prompt(question)
        new_player = Player(
            name = answers['name']
        )
        if new_player.name in [player[0] for player in player_name]:
            print("\x1b[35;3mYou're not new! Try logging in\x1b[35;0m")
            player_menu()
        else:
            session.add(new_player)
            session.commit()
            returning_player()



    def returning_player():
        print("\u001B[2m\u001B[36m---------------------------------------------------------------------------------------------------\u001B[2m\u001B[0m \n ")
        players = session.query(Player).all()
        returning_player_options = [
            inquirer.List("choose",
                        message = "\x1b[35;3mSelect Yourself\x1b[35;0m",
                        #   choices =[player for player in players],
                        choices=[(player.name) for player in players],
                        ),
        ]
        # print(players)
        answer = inquirer.prompt(returning_player_options)
        selected_player_name = answer["choose"]


        selected_player = session.query(Player).filter(Player.name == selected_player_name).first()

        logged_in_menu(selected_player)
        return selected_player


    

    def return_to_start ():
        print("\u001B[2m\u001B[36m---------------------------------------------------------------------------------------------------\u001B[2m\u001B[0m \n ")
        return_start = [
            inquirer.List("return",
                        message = "\x1b[35;3mWould you like to return to the Start menu?\x1b[35;0m",
                        choices = ["Yes", "No"],
                        ),
        ]
        return_start_answers = inquirer.prompt(return_start)
        if return_start_answers["return"] == "Yes":
            starter_menu()
        elif return_start_answers["return"] == "No":
            print("\x1b[35;3mYou'll never make the high scores like that!\x1b[35;0m \n")
            exit

        

    def logged_in_menu(selected_player):    #needs to take in player thats selected?
        print("\u001B[2m\u001B[36m---------------------------------------------------------------------------------------------------\u001B[2m\u001B[0m \n ")
        # print(f"Welcome {player.name}")
        # print(selected_player.name)
        start_menu = [
        inquirer.List("options",
                        message = f"\x1b[35;3mHello,\x1b[35;0m {selected_player.name}\x1b[35;3m! What do you want to do?\x1b[35;3m0m",
                        choices = ["Take Quiz", "View my Stats", "Change my Name", "Delete my Profile", "Log Out", "Quit"],
                        carousel=True,
                        ),
        ]

        start_menu_responses = inquirer.prompt(start_menu)
        start_menu_responses_key = start_menu_responses["options"]

        if start_menu_responses_key == "Take Quiz":
            select_quiz(selected_player)
        elif start_menu_responses_key == "View my Stats":
            view_player_stats(selected_player)
        elif start_menu_responses_key == "Change my Name":
            edit_player(selected_player)
        elif start_menu_responses_key == "Delete my Profile":
            delete_player(selected_player)
        elif start_menu_responses_key == "Log Out":
            print("\x1b[35;3mGo study and come back!\x1b[35;3m")
            starter_menu()
        elif start_menu_responses_key == "Quit":
            print("\x1b[35;3mQuitter!\x1b[35;0m \n")
            exit

    # STRETCH GOAL #1
    # def select_quiz_topic():
    #     pass
            

    def select_quiz(selected_player):
        print("\u001B[2m\u001B[36m---------------------------------------------------------------------------------------------------\u001B[2m\u001B[0m \n ")
        # print(selected_player.name)
        # quizzes = session.query(Quiz).all()

        select_quiz_options = [
        inquirer.List("choose",
                        message = "\x1b[35;3mHow smart do you think you are?\x1b[35;0m",
                        choices = ["Not Very", "I'm Average", "Like SO smart", "Marilyn Vos Savant", "Quit"]
                        ),
        ]

        answer = inquirer.prompt(select_quiz_options)
        answer_key = answer["choose"]
        # print(answer)
        # quiz = answer_key.id
        # selected_quiz = quiz

        if answer_key == "Not Very":
            new_easy_quiz = Quiz(name="Easy", player_id=selected_player.id)
            session.add(new_easy_quiz)
            session.commit()
            print("\x1b[35;3mThat's okay! We all start somewhere. Good luck!\x1b[35;0m")
            easy_quiz(selected_player, new_easy_quiz)
        elif answer_key == "I'm Average":
            new_medium_quiz = Quiz(name="Medium", player_id=selected_player.id)
            session.add(new_medium_quiz)
            session.commit()
            print("\x1b[35;3mLet's see it! 50%!\x1b[35;0m")
            medium_quiz(selected_player, new_medium_quiz)
        elif answer_key == "Like SO smart":
            new_hard_quiz = Quiz(name="Hard", player_id=selected_player.id)
            session.add(new_hard_quiz)
            session.commit()
            print("\x1b[35;3mLike OMG. I bet you are.\x1b[35;0m")
            hard_quiz(selected_player, new_hard_quiz)
        elif answer_key == "Marilyn Vos Savant":
            new_marilyn_vos_savant_quiz = Quiz(name="Marilyn Vos Savant", player_id=selected_player.id)
            session.add(new_marilyn_vos_savant_quiz)
            session.commit()
            print("\x1b[35;3mHaha! Bad Choice!\x1b[35;0m")
            marilyn_vos_savant_quiz(selected_player, new_marilyn_vos_savant_quiz)
        elif answer_key == "Quit":
            print("\x1b[35;3mChicken!\x1b[35;0m \n")
            exit



    def easy_quiz(selected_player, new_easy_quiz):
        print("\u001B[2m\u001B[36m---------------------------------------------------------------------------------------------------\u001B[2m\u001B[0m \n ")
        # print(new_easy_quiz)
        # print(selected_player)
        score = run_easy_quiz()
        result = Result(player_id=selected_player.id, quiz_id=new_easy_quiz.id, score=score)
        session.add(result)
        session.commit()
        post_quiz(selected_player)

    def medium_quiz(selected_player, new_medium_quiz):
        print("\u001B[2m\u001B[36m---------------------------------------------------------------------------------------------------\u001B[2m\u001B[0m \n ")
        score = run_medium_quiz()
        result = Result(player_id=selected_player.id, quiz_id=new_medium_quiz.id, score=score)
        session.add(result)
        session.commit()
        post_quiz(selected_player)

    def hard_quiz(selected_player, new_hard_quiz):
        print("\u001B[2m\u001B[36m---------------------------------------------------------------------------------------------------\u001B[2m\u001B[0m \n ")
        score = run_hard_quiz()
        result = Result(player_id=selected_player.id, quiz_id=new_hard_quiz.id, score=score)
        session.add(result)
        session.commit()
        post_quiz(selected_player)

    def marilyn_vos_savant_quiz(selected_player, new_marilyn_vos_savant_quiz):
        print("\u001B[2m\u001B[36m---------------------------------------------------------------------------------------------------\u001B[2m\u001B[0m \n ")
        score = run_marilyn_vos_savant_quiz()
        result = Result(player_id=selected_player.id, quiz_id=new_marilyn_vos_savant_quiz.id, score=score)
        session.add(result)
        session.commit()
        post_quiz(selected_player)
        


    def post_quiz (selected_player):
            print("\u001B[2m\u001B[36m---------------------------------------------------------------------------------------------------\u001B[2m\u001B[0m \n ")
            increment_times_played(selected_player)
            post_quiz_options = [
                inquirer.List("return",
                            message = "\x1b[35;3mNow what?\x1b[35;0m",
                            choices = ["Take another quiz", "My Profile", "Quit"],
                            ),
            ]
            return_start_answers = inquirer.prompt(post_quiz_options)
            if return_start_answers["return"] == "Take another quiz":
                select_quiz(selected_player)
            if return_start_answers["return"] == "My Profile":
                logged_in_menu(selected_player)
            elif return_start_answers["return"] == "Quit":
                print("\x1b[35;3mSee you next time!\x1b[35;3m \n")
                exit



    def edit_player(selected_player):
        print("\u001B[2m\u001B[36m---------------------------------------------------------------------------------------------------\u001B[2m\u001B[0m \n ")
        # print(selected_player)
        player_id = selected_player.id
        player = session.query(Player).filter_by(id = player_id).first()
        name = input("\x1b[35;3mEnter a new name or press enter to keep current name: \x1b[35;0m")
        if name:
                player.name = name
        session.commit()
        logged_in_menu(selected_player)



    def delete_player(selected_player):
        print("\u001B[2m\u001B[36m---------------------------------------------------------------------------------------------------\u001B[2m\u001B[0m \n ")
        player_id = selected_player.id
        player = session.query(Player).filter_by(id = player_id).first()
        start_menu = [
        inquirer.List("options",
                        message = "\x1b[35;3mAre you sure you want to delete yourself?\x1b[35;3m",
                        choices = ["No, go back!", "Yes"],
                        ),
        ]
        start_menu_responses = inquirer.prompt(start_menu)
        start_menu_responses_key = start_menu_responses["options"]
        if start_menu_responses_key == "No, go back!":
            logged_in_menu(selected_player)
        elif start_menu_responses_key == "Yes":
            session.delete(player)
            session.commit()
            print("\x1b[35;3mYou're ouuutta here!\x1b[35;3m \n")
            starter_menu()
            


    def high_scores():
        players = session.query(Player).all()
        all_scores = session.query(Result).all()
        # all_quizzes = session.query(Quiz).all()
        player_name = session.query(Player).filter(Player.id == Result.player_id).first()
        quiz_name = session.query(Quiz).filter(Quiz.id == Result.quiz_id).first()
        all_scores1 = [(result.score, player_name.name, quiz_name.name) for result in all_scores]

        sorted_list = sorted(all_scores1, key = lambda k: k[0], reverse = True)
        if not players:
            print("\x1b[35;3mThere are no exsisting players\x1b[35;3m")
        else:
            print(f"""
\u001B[2m\u001B[36m---------------------------------------------------------------------------------------------------\u001B[2m\u001B[0m
\u001B[1m\u001B[36m     
░█─░█ ─▀─ █▀▀▀ █──█ 　 ░█▀▀▀█ █▀▀ █▀▀█ █▀▀█ █▀▀ █▀▀ 
░█▀▀█ ▀█▀ █─▀█ █▀▀█ 　 ─▀▀▀▄▄ █── █──█ █▄▄▀ █▀▀ ▀▀█ 
░█─░█ ▀▀▀ ▀▀▀▀ ▀──▀ 　 ░█▄▄▄█ ▀▀▀ ▀▀▀▀ ▀─▀▀ ▀▀▀ ▀▀▀\u001B[1m\u001B[36m
              
🥇 \x1b[33m{sorted_list[0][1]}\x1b[0m is \x1b[33;1mTop Dawg\x1b[33;0m with \x1b[37;1m{sorted_list[0][0]}\x1b[37;0m \u001B[90m({sorted_list[0][2]})\u001B[0m
🥈 \x1b[32m{sorted_list[1][1]}\x1b[0m has \x1b[32;1mMedium Bucks\x1b[32;0m with \x1b[37;1m{sorted_list[1][0]}\x1b[37;0m \u001B[90m({sorted_list[1][2]})\u001B[0m
🥉 \u001B[34m{sorted_list[2][1]}\u001B[0m is \u001B[1m\u001B[34mKinda Smart\u001B[1m\u001B[0m with \x1b[37;1m{sorted_list[2][0]}\x1b[37;0m \u001B[90m({sorted_list[2][2]})\u001B[0m\n
\x1b[35;3mIf you ain't up here, you're a\x1b[35;0m \x1b[31;1msmall fry\x1b[31;0m!\u001B[0m
            """)
            return_to_start()

    


    def view_player_stats(selected_player):
        print("\u001B[2m\u001B[36m---------------------------------------------------------------------------------------------------\u001B[2m\u001B[0m \n ")
        print(f"{selected_player.name}'s STATS\n")
        print(f"Player ID: {selected_player.id}")
        print(f"Times Played: {selected_player.times_played}")
        print(f"Avg Score: {selected_player.avg_score}")
        print(f"High Score: {selected_player.high_score}\n")
        logged_in_menu(selected_player)


    def increment_times_played(selected_player):
        session.query(Player).all()
        if selected_player.id == Player.id:
            selected_player = Player
        # print(selected_player.times_played)

        if selected_player.times_played is None:
            selected_player.times_played = 1
        else:
            selected_player.times_played += 1
        session.commit()
        player_avg_score(selected_player)
        player_high_score(selected_player)



    def player_avg_score(selected_player):
        # Query all results for this player
        results = session.query(Result).filter_by(player_id=selected_player.id).all()

        if results:
            total_score = sum(result.score for result in results)
            selected_player.avg_score = int(total_score / len(results))
        else:
            selected_player.avg_score = 0
        session.commit()


    def player_high_score(selected_player):
        # Query all results for this player
        results = session.query(Result).filter_by(player_id=selected_player.id).all()

        if results:
            selected_player.high_score = max(result.score for result in results)
        else:
            selected_player.high_score = 0
        session.commit()


    starter_menu()