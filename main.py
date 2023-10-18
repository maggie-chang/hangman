import pgzrun
import random

max_wrong_guesses = 10


WIDTH = 500
HEIGHT = 300


#def draw():
    #screen.fill((255, 255, 255))
    #spooky_word = get_random_spooky_word()
    #print(spooky_word)
    #screen.draw.text(spooky_word, (250, 150), color="red")


def get_random_spooky_word():
    '''returns a random word from words.txt'''
    with open("words.txt") as file:
        return random.choice(list(file))[:-1]
  

def is_only_letters(word):
    '''makes sure players' input is only letters'''
    for letter in word:
        if letter not in "a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z":
         return False
    return True

def word_place_clues(spooky_word, guessed_word, guessed_letter):
    spooky_word = get_random_spooky_word
    if guessed_word == spooky_word
        return print("you won!")

    word_placement = []
        for letter in guessed_letter:
            if guessed_letter[] == len(spooky_word)[]
                return len(spooky_word)[]
            elif

    
    



print("this is hangman")
print("enter letters and guess word")


while True:

    spooky_word = get_random_spooky_word()
    num_letters = len(spooky_word)
    print(f"spooky word is {spooky_word}")

    wrong_guesses_taken = 0
    while wrong_guesses_taken < max_wrong_guesses:
        letter_guess = ""
        while len(letter_guess) != int(max_wrong_guesses) or not is_only_letters:
            letter_guess = input()




pgzrun.go()
