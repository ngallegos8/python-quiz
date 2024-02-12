QUESTIONS = {
    "The word 'aprosexia' means which of the following?": [
        "The inability to concentrate on anything", "The inability to make decisions", "A feverish desire to rip one's clothes off", "The inability to stand up"
    ],
    "Which film star has his statue in Leicester Square?": [
        "Charlie Chaplin", "Paul Newman", "Rowan Atkinson ", "Alfred Hitchcock"
    ],
    "Which of the following  British Monarchs never appeared on a circulated pound sterling coin?": [
        "Edward VIII", "Victoria", "George VI", "Charles II"
    ],
    "Which musician has collaborated with American producer Porter Robinson and released the 2016 song 'Shelter'?": [
        "Madeon", "Mat Zo", "deadmau5", "Zedd"
    ],
    "The words 'bungalow' and 'shampoo' originate from the languages of which country?": [
        "India", "Papua New Guinea", "Ethiopia", "China"
    ],
    "What is the most commonly used noun in the English language?": [
        "Time", "Home", "Water", "Man"
    ],
    "The word 'astasia' means which of the following?": [
        "The inability to stand up", "The inability to make decisions", "The inability to concentrate on anything", "A feverish desire to rip one&#039;s clothes off"
    ],
    "According to Fair Works Australia, how long do you have to work to get Long Service Leave?": [
        "7 years", "2 years", "8 years", "6 months"
    ],
    "According to the 2014-2015 Australian Bureau of Statistics, what percentage of Australians were born overseas?": [
        "28%", "13%", "20%", "7%"
    ],
    "If you planted the seeds of Quercus robur, what would grow?": [
        "Trees", "Grains", "Vegetables", "Flowers"
    ],
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