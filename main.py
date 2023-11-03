# import pgzrun
import random

max_wrong_guesses = 10


WIDTH = 500
HEIGHT = 300


# def draw():
# screen.fill((255, 255, 255))
# spooky_word = get_random_spooky_word()
# print(spooky_word)
# screen.draw.text(spooky_word, (250, 150), color="red")

def introduction():
    print("""
          Welcome to Hangman!

Instructions and Info:
    -  All words are anything related to the fall season
    - There will be asterisks '*' indicating the # of letters in the word
    - For each incorrect letter guessed, a body part will be added
                    """)
    return True
    


def get_random_spooky_word():
    """returns a random word from words.txt"""
    with open("words.txt") as file:
        return random.choice(list(file))[:-1]


def is_only_letters(word):
    """makes sure players' input is only letters"""
    for letter in word:
        if (
            letter
            not in "a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z"):
            return False
    return True


def correct_word(spooky_word, guessed_word):
    """returns "you won!" when the player correctly guesses the spooky word"""
    spooky_word = get_random_spooky_word
    if guessed_word == spooky_word:
        return print("""
________
| /     |
|
|   
|      (:D)
|      \ | /
|        | 
|        |
|____+  / \
you saved the man!""")


def clues_from_letter(spooky_word: str, guessed_letter):
    clue = ""
    guess_index = spooky_word.index(guessed_letter)

    for i in range(len(spooky_word)):
        if i == guess_index:
            clue += guessed_letter
        else:
            clue += "*"

    return clue


def string_to_array(str):
    result = []
    for char in str:
        result.append("*")
    return result



def play():

    while True:
        spooky_word = get_random_spooky_word()
        print(f"spooky word is {spooky_word}")

        wrong_guesses_taken = 0
        while wrong_guesses_taken <= max_wrong_guesses:
            guess = ""
            # print(clues_from_letter(guess, spooky_word))
            print(string_to_array(spooky_word))

            while wrong_guesses_taken != max_wrong_guesses or not is_only_letters(guess):
                print(f"you have {wrong_guesses_taken} wrong guess(es) taken")
                guess = input("enter a letter: ")

            if guess in spooky_word:
                pass

            if wrong_guesses_taken == 1:
                print("""""")

            while wrong_guesses_taken == max_wrong_guesses:
                word_guess = input(
                    "This is your last attempt. Make a *word* guess: ")

                # if the letter the player inputs is not in the word, returns *
                if word_guess == correct_word:
                    break
                elif wrong_guesses_taken > max_wrong_guesses:
                    print(f"""you lost...
    ________
    | /     |
    |            
    |
    |
    |
    |
    |              
    |____+{(0_0)}
    the answer was {spooky_word}""")
                    break

            wrong_guesses_taken += 1

            if wrong_guesses_taken > max_wrong_guesses:
                print(f"you lost the answer is {spooky_word}")


#############################################################################################
# MAIN PROGRAM
#############################################################################################
introduction()
play()
#spooky_word = get_random_spooky_word()
#print(string_to_array(spooky_word))
# pgzrun.go()


# *important* missing:
# 1) giving player “*”s (shows len of spooky_word) at start of game
# 2) using player's input then returning whether if the guess is correct or incorrect
#   - if correct, returns the player's letter input and gives the player the right position.
#   - if wrong, wrong_guesses_taken += 1, and returns the same string of *s (and letters) as before & look at #4
# 4) assign each hangman image each of the wrong_guesses_taken += 1
#   - e.g. when wrong_guesses taken = 0, it will print the first image of the hangman, which is just the hanger because no wrong guesses has been taken
# 5) play again option + give up option
