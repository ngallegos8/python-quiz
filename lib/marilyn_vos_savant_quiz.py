from string import ascii_lowercase

QUESTIONS = {
    "In 'Resident Evil 3', how many inventory slots does Jill have at the start of the game?": ["10"],
    "How many calories are in a 355 ml can of Pepsi Cola?": ["150"],
    "The Swedish word 'Grunka' means what in English?": ["Thing"],
    "Located in Chile, El Teniente is the world's largest underground mine for what metal?": ["Copper"],
    "In 'Battle Cats', what is Moneko / MISS Moneko's critical percentage rate?": ["15%"],
    "The words 'bungalow' and 'shampoo' originate from the languages of which country?": ["India"],
    "According to the 2014-2015 Australian Bureau of Statistics, what percentage of Australians were born overseas?": ["28%"],
    "What is the weight of a Gold Bar in Fallout: New Vegas?": ["35 Pounds"],
    "What is the romanized Arabic word for 'moon'?": ["Qamar"],
    "How long did it take the motorized window washers of the original World Trade Center to clean the entire exterior of the building?": ["1 Month"]
}

# def run_marilyn_vos_savant_quiz():
#     for question, correct_answer in QUESTIONS:
#         answer = input(f"{question}? ")
#         if answer == correct_answer:
#             print("Correct!")
#         else:
#             print(f"The answer is {correct_answer!r}, not {answer!r}")

def run_marilyn_vos_savant_quiz():

    num_correct = 0
    for num, (question, alternatives) in enumerate(QUESTIONS.items(), start=1):
        print(f"\nQuestion {num}:")
        print(f"{question}?")
        correct_answer = alternatives[0]

        answer = input("\n??? ")
        if answer == correct_answer:
            num_correct += 1
            print("⭐ Correct! ⭐")
        else:
            print(f"The answer is {correct_answer!r}, not {answer!r}")
        

    print(f"\nYou got {num_correct} correct out of {num} questions\n")
    return num_correct