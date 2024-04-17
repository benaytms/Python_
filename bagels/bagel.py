def introduction() -> dict[str]:
    quotes = {
        "q1": "Bagels, a deductive logic game.",
        "q2": "By AI Sweigart\n",
        "q3": "I am thinking of a 3-digit number. Try to guess what it is.",
        "clues": "Here are some clues: \n",
        "clue1": "When i say: Pico      That means: One digit is correct but"
        " in the wrong position\n",
        "clue2": "When i say: Fermi     That means: One digit is correct and"
        " in the right position.\n",
        "clue3": "When i say: Bagels    That means: No digit is correct\n",
        "start": "I have thought up a number",
        "guesses": "    You have 10 guesses to get it."
    }

    print(quotes['q1'])
    print(quotes['q2'])
    print(quotes['q3'])
    print(quotes['clues'])
    print(quotes['clue1'])
    print(quotes['clue2'])
    print(quotes['clue3'])
    print(quotes['start'])
    print(quotes['guesses'])


def game_itself():
    introduction()
    
    

def main_caller():
    game_itself()

if __name__ == "__main__":
    main_caller()