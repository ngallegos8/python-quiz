from string import ascii_lowercase
import string

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
        print(f"\nQuestion {num}:")
        print(f"{question}?")
        correct_answer = alternatives[0]
        labeled_alternatives = dict(zip(ascii_lowercase, sorted(alternatives)))
        for label, alternative in labeled_alternatives.items():
            print(f"  {label}) {alternative}")

        answer_label = input("\nChoice? ")
        answer = labeled_alternatives.get(answer_label)
        if answer == correct_answer:
            num_correct += 1
            print("⭐ Correct! ⭐")
        else:
            print(f"The answer is {correct_answer!r}, not {answer!r}")
        

    print(f"\nYou got {num_correct} correct out of {num} questions")
    return num_correct