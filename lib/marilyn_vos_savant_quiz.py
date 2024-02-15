from string import ascii_lowercase

QUESTIONS = {
    "In 'Resident Evil 3', how many inventory slots does Jill have at the start of the game? \u001B[90m(Int)\u001B[0m": ["10"],
    "How many calories are in a 355 ml can of Pepsi Cola? \u001B[90m(Int)\u001B[0m": ["150"],
    "The Swedish word 'Grunka' means what in English?": ["Thing"],
    "Located in Chile, El Teniente is the world's largest underground mine for what metal?": ["Copper"],
    "In 'Battle Cats', what is Moneko / MISS Moneko's critical percentage rate? \u001B[90m(Int & unit)\u001B[0m": ["15%"],
    "The words 'bungalow' and 'shampoo' originate from the languages of which country?": ["India"],
    "According to the 2014-2015 Australian Bureau of Statistics, what percentage of Australians were born overseas? \u001B[90m(Int & unit)\u001B[0m": ["28%"],
    "What is the weight of a Gold Bar in Fallout: New Vegas? \u001B[90m(Int & unit)\u001B[0m": ["35 Pounds"],
    "What is the romanized Arabic word for 'moon'?": ["Qamar"],
    "How long did it take the motorized window washers of the original World Trade Center to clean the entire exterior of the building? \u001B[90m(Int & unit)\u001B[0m": ["1 Month"]
}

def run_marilyn_vos_savant_quiz():

    num_correct = 0
    for num, (question, alternatives) in enumerate(QUESTIONS.items(), start=1):
        print(f"\n\u001b[4m\u001b[37;1mQuestion {num}:\u001b[0m")
        print(f"\n{question}?")
        correct_answer = alternatives[0]

        answer = input("\n??? ")
        if answer == correct_answer:
            num_correct += 1
            print("\u001B[3m\n\u001b[32mCorrect!\u001B[3m\u001b[0m ✅\n")
        else:
            print(f"\n \u001B[3m\u001b[1mHA!\u001B[3m\u001b[0m \u001B[3m\x1b[37;1;4mNOPE!\u001B[3m\x1b[37;1;0m \u001B[3mThe answer is\u001B[3m\u001B[0m \u001b[32m{correct_answer!r}\u001b[0m, \u001B[3m\u001B[3mnot\u001B[3m\u001B[0m \u001b[31m{answer!r}\u001b[0m\n")
        

    general_print = print(f"\nYou got {num_correct} correct out of {num} questions\n")   
    if num_correct <= 3:
        general_print
        print("\u001B[3mOugh! Maybe you're actually 'Like SO smart'...that quiz might be better for you...\u001B[0m")
    elif 3 < num_correct <= 7:
        general_print
        print("\u001B[3mSmarter than my dog!\u001B[0m")
    elif 7 < num_correct <= 9:
        general_print
        print("\u001B[3mI'm actually impressed. That's hard to do.\u001B[0m")
    elif num_correct == 10:
        general_print
        print("\u001B[3mCheater!\u001B[0m")
    return num_correct