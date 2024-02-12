QUESTIONS = {
    "Which one of the following rhythm games was made by Harmonix?": [
        "Rock Band", "Meat Beat Mania", "Guitar Hero Live", "Dance Dance Revolution"
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

for question, alternatives in QUESTIONS.items():
    correct_answer = alternatives[0]
    sorted_alternatives = sorted(alternatives)
    for label, alternative in enumerate(sorted_alternatives):
        print(f"  {label}) {alternative}")

    answer_label = int(input(f"{question}? "))
    answer = sorted_alternatives[answer_label]
    if answer == correct_answer:
        print("Correct!")
    else:
        print(f"The answer is {correct_answer!r}, not {answer!r}")