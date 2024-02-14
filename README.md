# python-quiz

PYTHON QUIZ

Test yourself on general knowledge, create a username , choose your difficulty of trivia and keep track of your scores

HOW TO USE

REQUIREMENTS
1. Ensure you have python, pipenv and python-inquirer installed on your system

INSTALLATION
2. Navigate to the python-quiz directory installed on your system
3. Run the command 'pipenv install' to install dependencies
4. Run the command 'pipenv shell' to open a shell enviroment
5. If you don't have python-inquirer installed run 'pip install inquirer'

RUN THE QUIZ
6. With the shell enviroment open (Step 4), run the command 'python3 lib/cli.py'

MAIN MENU
Choose to Play, View High Scores or Quit

VIEW HIGH SCORES
Displays 3 highest scores from all players and all quizzes taken
Option to return to main menu or quit

LOG IN
If you are a new player first create yourself, once created or if returning select yourself from the list of all users
Once logged in your page dsplays options to Take Quiz, Edit your player name, Delete your player profile or Quit the app

TAKE A QUIZ
Select a difficulty and quiz will start
    (Note on difficulties:
        EASY, MEDIUM, HARD: Multiple choice
        MARILYN VOS SAVANT: Input-based. This test is the most difficult questions AND has no options.
                            You must enter the correct answer. Punctuation, grammar and units MUST be correct!!!
                            If you're truly smart enough, you'll know how to write these correctly anyways)
After each question, you will either be notified with "Correct!" or a wrong answer message telling you your incorrect choice and what the correct answer is.
    If you enter a choice outside of the given (i.e. 'e' with mutiple choice options 'a-d', your incorrect answer will show as "None")
End of quiz will display your result as a score (#correct answers out of 10)
Your result will be added to the Result table and affect your player (and quiz difficulty) stats

POST QUIZ
Options to play again, go back to your profile or quit the game

RESOURCES USED
Python Inquirer Documantation: https://python-inquirer.readthedocs.io/en/latest/usage.html#the-prompter
Flatiron School Phase 3 Modules: https://learning.flatironschool.com/courses/7036/modules
Stack Overflow (helped restructure my tables to wok cohesively): https://stackoverflow.com/questions/9607803/best-method-for-storing-quiz-results-in-mysql
SQLAlchemy Documentation: https://docs.sqlalchemy.org/en/20/orm/basic_relationships.html#one-to-many
Stephen Lambert & David Doan: Flatiron instrcutors helped with troubleshooting errors








Make sure you have python and pipenv installed on your system
Navigate to the specialty-coffee-manager directory in the terminal
Run the command pipenv install and then open a shell enrivonment using pipenv shell
With the shell environment open, enter the command 'python3 lib/app.py'









Flatiron Phase 3 CLI Project

