     import pgzrun
import random

max_wrong_guesses = 10


WIDTH = 500
HEIGHT = 300


# def draw():
# screen.fill((255, 255, 255))
# spooky_word = get_random_spooky_word()
# print(spooky_word)
# screen.draw.text(spooky_word, (250, 150), color="red")


def get_random_spooky_word():
    """returns a random word from words.txt"""
    with open("words.txt") as file:
        return random.choice(list(file))[:-1]


def is_only_letters(word):
    """makes sure players' input is only letters"""
    for letter in word:
        if (letter not in "a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z"):
            return False
    return True


def correct_word(spooky_word, guessed_word):
    '''returns "you won!" when the player correctly guesses the spooky word'''
    spooky_word = get_random_spooky_word
    if guessed_word == spooky_word:
        return print("you won!")


def clues_from_letter(spooky_word: str, guessed_letter):
    clue = ""
    guess_index = spooky_word.index(guessed_letter)

    for i in range(len(spooky_word)):
        if i == guess_index:
            clue += guessed_letter
        else:
            clue += "*"

    return clue

def hangman(man1, man2, man3, man4, man5, man6, hang7, hang8, hang9, hang10, spooky_word, ):





print("This is HANGMAN. A simple game where you can guess the letter")

while True:
    spooky_word = get_random_spooky_word()
    num_letters = len(spooky_word)
    print(f"spooky word is {spooky_word}")


    wrong_guesses_taken = 0
    while wrong_guesses_taken < max_wrong_guesses:
        guess = ""
        print(clues_from_letter(guess, spooky_word))

        while guess != int(max_wrong_guesses) or not is_only_letters:
            print(f"you have {wrong_guesses_taken} wrong guess(es) taken")
            guess = input("enter a letter: ")
        
        #if the letter the player inputs is not in the word, returns *
        print(clues_from_letter(guess, spooky_word))
        max_wrong_guesses += 1
        
        if correct_word == guess:
            break
        if guess >= max_wrong_guesses:
            print(f"you lost the answer was {spooky_word}")

pgzrun.go()





#missing:
# 1) giving player *s (shows len of spooky_word) at start of game
# 2) using player's input then returns whether if its correct or incorrect  ; 
#   if correct, returns player's letter input and gives player right position. 
#   if wrong, wrong_guesses_taken += 1, and returns the same string of *s   (and letters) as before
# 4) play again option
# 5) 