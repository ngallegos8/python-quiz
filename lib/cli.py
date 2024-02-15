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



    def returning_player():
        players = session.query(Player).all()
        returning_player_options = [
            inquirer.List("choose",
                        message = "Select Yourself",
                        #   choices =[player for player in players],
                        choices=[(player.name) for player in players],  # Display player names in the list
                        ),
        ]
        # print(players)
        answer = inquirer.prompt(returning_player_options)
        selected_player_name = answer["choose"]
        # print(answer_key)
        # player = answer_key
        # print(type(player))
        # selected_player = player
        selected_player = session.query(Player).filter(Player.name == selected_player_name).first()
        # print(selected_player)

        logged_in_menu(selected_player)
        return selected_player

    # def returning_player(session):
    #     players = session.query(Player).all()
    #     returning_player_options = [
    #         inquirer.List(
    #             "choose",
    #             message="Select Yourself",
    #             choices=[(player.id, player.name) for player in players],  # Display player names in the list
    #             carousel=True,  # Allow scrolling through the list
    #         ),
    #     ]
    #     answer = inquirer.prompt(returning_player_options)
    #     player_id = answer["choose"]
        
    #     # Find the selected player object based on the selected player ID
    #     selected_player = session.query(Player).filter(Player.id == player_id).first()

    #     # print(selected_player)
    #     return selected_player
    

    # # # Example usage:
    # # # Assuming you have created a session named session
    # selected_player = returning_player(session)
    # print(selected_player)  # This should print the selected player object with all its attributes



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
        # print(selected_player.name)
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
        # print(selected_player.name)
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
            new_easy_quiz = Quiz(name="Easy", player_id=selected_player.id)
            session.add(new_easy_quiz)
            session.commit()
            easy_quiz(selected_player, new_easy_quiz)
        elif answer_key == "Medium":
            new_medium_quiz = Quiz(name="Medium", player_id=selected_player.id)
            session.add(new_medium_quiz)
            session.commit()
            medium_quiz(selected_player, new_medium_quiz)
        elif answer_key == "Hard":
            new_hard_quiz = Quiz(name="Hard", player_id=selected_player.id)
            session.add(new_hard_quiz)
            session.commit()
            hard_quiz(selected_player, new_hard_quiz)
        elif answer_key == "Marilyn Vos Savant":
            new_marilyn_vos_savant_quiz = Quiz(name="Marilyn Vos Savant", player_id=selected_player.id)
            session.add(new_marilyn_vos_savant_quiz)
            session.commit()
            marilyn_vos_savant_quiz(selected_player, new_marilyn_vos_savant_quiz)
        elif answer_key == "Quit":
            print("Chicken!")
            exit



    def easy_quiz(selected_player, new_easy_quiz):
        # print(new_easy_quiz)
        # print(selected_player)
        score = run_easy_quiz()
        result = Result(player_id=selected_player.id, quiz_id=new_easy_quiz.id, score=score)
        session.add(result)
        session.commit()
        post_quiz(selected_player)

    def medium_quiz(selected_player, new_medium_quiz):
        score = run_medium_quiz()
        result = Result(player_id=selected_player.id, quiz_id=new_medium_quiz.id, score=score)
        session.add(result)
        session.commit()
        post_quiz(selected_player)

    def hard_quiz(selected_player, new_hard_quiz):
        score = run_hard_quiz()
        result = Result(player_id=selected_player.id, quiz_id=new_hard_quiz.id, score=score)
        session.add(result)
        session.commit()
        post_quiz(selected_player)

    def marilyn_vos_savant_quiz(selected_player, new_marilyn_vos_savant_quiz):
        score = run_marilyn_vos_savant_quiz()
        result = Result(player_id=selected_player.id, quiz_id=new_marilyn_vos_savant_quiz.id, score=score)
        session.add(result)
        session.commit()
        post_quiz(selected_player)
        


    def post_quiz (selected_player):
            increment_times_played(selected_player)
            post_quiz_options = [
                inquirer.List("return",
                            message = "Now what?",
                            choices = ["Take another quiz", "My Profile", "Quit"],
                            ),
            ]
            return_start_answers = inquirer.prompt(post_quiz_options)
            if return_start_answers["return"] == "Take another quiz":
                select_quiz(selected_player)
            if return_start_answers["return"] == "My Profile":
                logged_in_menu(selected_player)
            elif return_start_answers["return"] == "Quit":
                print("See you next time!")
                exit



    def edit_player(selected_player):
        # print(selected_player)
        player_id = selected_player
        player = session.query(Player).filter_by(id = player_id).first()
        name = input("Enter a new name or press enter to keep current name: ")
        if name:
                player.name = name
        session.commit()
        logged_in_menu(selected_player)



    def delete_player(selected_player):
        player_id = selected_player
        player = session.query(Player).filter_by(id = player_id).first()
        start_menu = [
        inquirer.List("options",
                        message = "Are you sure you want to delete yourself?",
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
            print("You're outta here!")
            starter_menu()
            


    def high_scores():
        players = session.query(Player).all()
        all_scores = session.query(Result).all()
        player_name = session.query(Player).filter(Player.id == Result.player_id).first()
        all_scores1 = [(result.score, player_name.name) for result in all_scores]

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







    # def results(selected_player):
    #     return [result for result in Result.all if result.player_id == selected_player.id]
    
    # # def games_played(selected_player):
    # #     return set([result for result in Result.all if result.quiz_id == selected_player])

    # def times_played(selected_player, results):
    #     num_times_played =  len(results)
    #     num_times_played = selected_player.times_played

    # def add_times_played(selected_player):
    #     if selected_player.id == Player.id:
    #         Player.times_played = times_played

    

    def increment_times_played(selected_player):
        session.query(Player).all()
        if selected_player.id == Player.id:
            selected_player = Player
        print(selected_player.times_played)

        if selected_player.times_played is None:
            selected_player.times_played = 1
        else:
            selected_player.times_played += 1
        session.commit()
        



    # def results(self):
    #     return [result for result in Result.all if result.player == self]

    # def games_played(self):
    #     # return set([result for result in Result.all if result.game == self])
    #     return list({result.game for result in self.results()})

    # def played_game(self, game):
    #     return game in self.games_played()

    # def num_times_played(self, game):
    #     games_played = [result.game for result in self.results()]
    #     return games_played.count(game)










    starter_menu()