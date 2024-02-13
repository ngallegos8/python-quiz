from string import ascii_lowercase
import string

# OLD VERSION - Input has to be integer of index (i.e. 1, 2, 0)...wouldn't make sense to someone who doesn't understand indexes (0 = 1st choice)
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

QUESTIONS = {
    "Which one of the following rhythm games was made by Harmonix?": [
        "Rock Band", "Meat Beat Mania", "Guitar Hero Live", "Dance Dance Revolution"
        # dict(zip(string.ascii_lowercase, ["Rock Band", "Meat Beat Mania", "Guitar Hero Live", "Dance Dance Revolution"]))
    ],
    "What machine element is located in the center of fidget spinners?": [
        "Bearings", "Axles", "Gears", "Belts"
    ],
    "Which American-owned brewery led the country in sales by volume in 2015?": [
        "D. G. Yuengling and Son, Inc", "Anheuser Busch", "Boston Beer Company", "Miller Coors"
    ],
    "What is Tasmania?": [
        "An Australian State", "A flavor of Ben and Jerry's ice-cream", "A Psychological Disorder", "The Name of a Warner Brothers Cartoon Character"
    ],
    "What is the Zodiac symbol for Gemini?": [
      "Twins", "Fish", "Scales", "Maiden"
    ],
    "When one is 'envious', they are said to be what color?": [
        "Green", "Red", "Blue", "Yellow"
    ],
    "Who invented the first ever chocolate bar, in 1847?": [
        "Joseph Fry", "Andrew Johnson", "John Cadbury", "John Tyler"
    ],
    "Which of these colours is NOT featured in the logo for Google?": [
        "Pink", "Yellow", "Blue", "Green"
    ],
    "How would one say goodbye in Spanish?": [
        "Adiós","Hola", "Au Revoir", "Salír"
    ],
    "In the video-game franchise Kingdom Hearts, the main protagonist, carries a weapon with what shape?": [
        "Key", "Sword", "Pen", "Cellphone"
    ]
}

def run_easy_quiz():
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
# print(run_easy_quiz())


    