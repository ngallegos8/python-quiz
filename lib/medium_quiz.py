from string import ascii_lowercase

QUESTIONS = {
    "What is the defining characteristic of someone who is described as hirsute?": [
        "Hairy", "Rude", "Funny", "Tall"
    ],
    "What is the name of the very first video uploaded to YouTube?": [
        "Me at the zoo",
        "tribute",
        "carrie rides a truck",
        "Her new puppy from great grandpa vern."
    ],
    "What is the world's most expensive spice by weight?": [
        "Saffron", "Cinnamon", "Cardamom", "Vanilla"
    ],
    "What did the Spanish autonomous community of Catalonia ban in 2010, that took effect in 2012?": [
        "Bullfighting", "Fiestas", "Flamenco", "Mariachi"
    ],
    "Which of these words means 'idle spectator?'": [
        "Gongoozler", "Gossypiboma", "Jentacular", "Meupareunia"
    ],
    "What is the name of the popular animatronic singing fish prop, singing such hits such as 'Don't Worry, Be Happy'?": [
        "Big Mouth Billy Bass" "Big Billy Bass", "Singing Fish", "Sardeen"
    ],
    "Rolex is a company that specializes in what type of product?": [
        "Watches", "Cars", "Computers", "Sports equipment"
    ],
    "In the Morse code, which letter is indicated by 3 dots?": [
        "S", "O", "A", "C"
    ],
    "In a standard set of playing cards, which is the only king without a moustache?": [
        "Hearts", "Spades", "Diamonds", "Clubs"
    ],
    "What is the unit of currency in Laos?": [
        "Kip", "Ruble", "Konra", "Dollar"

    ]
}
def run_medium_quiz():

    num_correct = 0
    for num, (question, alternatives) in enumerate(QUESTIONS.items(), start=1):
        print(f"\n\u001b[4m\u001b[37;1mQuestion {num}:\u001b[0m")
        print(f"\n{question}?")
        correct_answer = alternatives[0]
        labeled_alternatives = dict(zip(ascii_lowercase, sorted(alternatives)))
        for label, alternative in labeled_alternatives.items():
            print(f"  {label}) {alternative}")

        answer_label = input("\nChoice? ")
        answer = labeled_alternatives.get(answer_label)
        if answer == correct_answer:
            num_correct += 1
            print("\u001B[3m\n\u001b[32mCorrect!\u001B[3m\u001b[0m ✅\n")
        else:
            print(f"\n \u001B[3m\u001b[1mHA!\u001B[3m\u001b[0m \u001B[3m\x1b[37;1;4mNOPE!\u001B[3m\x1b[37;1;0m \u001B[3mThe answer is\u001B[3m\u001B[0m \u001b[32m{correct_answer!r}\u001b[0m, \u001B[3m\u001B[3mnot\u001B[3m\u001B[0m \u001b[31m{answer!r}\u001b[0m\n")
        
    general_print = print(f"\nYou got {num_correct} correct out of {num} questions\n")   
    if num_correct <= 3:
        general_print
        print("\u001B[3mOugh! Maybe you're actually 'Not Very' smart...that quiz might be better for you...\u001B[0m")
    elif 3 < num_correct <= 7:
        general_print
        print("\u001B[3mWay to go! Right in the middle! How average of you!\u001B[0m")
    elif 7 < num_correct <= 9:
        general_print
        print("\u001B[3mGood but..they were only average level questions so... \u001B[0m")
    elif num_correct == 10:
        general_print
        print("\u001B[3mMaybe you're 'Like SO smart'! Take that quiz and let's see!\u001B[0m")
    return num_correct

    