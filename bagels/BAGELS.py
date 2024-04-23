# Credits: Big book small python projects
# game from Al Sweigart.

import random

NUM_DIGITS = 3
MAX_GUESSES = 10

def introduction() -> None:
    print('''Bagels, a deductive logic game.
By Al Sweigart.
          
I am thinking of a {}-digit number with no repeated digits.
Try to guess which number it is. Here are some clues:
When i say:     That means:
  PICO        One digit is correct but in the wrong position
  FERMI       One digit is correct and in the right position
  BAGELS      No digit is correct.
        
For Example, if the secret number was 248 and your guess was 843, the
clues would be FERMI PICO.'''.format(NUM_DIGITS))


def game_itself() -> None:

    introduction()
    
    while True:
        secretNum = getSecretNum()
        print('I have thought up a number')
        print(' You have {} guesses to get it\n'.format(MAX_GUESSES))

        num_guesses = 1
        while num_guesses <= MAX_GUESSES:
            guess = ''
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print("Guess #{}".format(num_guesses))
                guess = input('> ')
            
            clue = getClue(guess, secretNum)
            if clue == 'victory':
                break
            print(clue)
            num_guesses+=1

            if guess == secretNum:
                break
            if num_guesses > MAX_GUESSES:
                print("Guesses over!")
                print("The answer was ", secretNum)

        print("Do you wish to play again? Y/N")
        if input('> ').lower() != 'y':
            break

    print("Thanks for playing!")


def getSecretNum():

    numbers = list('0123456789')
    random.shuffle(numbers)
    secretNum = numbers[:3]
    return secretNum

def getClue(guess, secretNum):
    
    if list(guess) == secretNum:
        print("You Won!")
        return 'victory'
    
    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('FERMI')
        elif guess[i] in secretNum:
            clues.append('PICO')
        
    if len(clues) == 0:
        return 'BAGELS'
    else:
        clues.sort()
        return ' '.join(clues)
    

def main_caller() -> None:
    game_itself()

if __name__ == "__main__":
    main_caller()