import pgzrun
import random

MAX_WRONG_GUESSES = 10


WIDTH = 500
HEIGHT = 300


#def draw():
    #screen.fill((255, 255, 255))
    #spooky_word = get_random_spooky_word()
    #print(spooky_word)
    #screen.draw.text(spooky_word, (250, 150), color="red")


def get_random_spooky_word():
    with open("words.txt") as file:
        return random.choice(list(file))[:-1]
  

def is_only_letters(word):
    for letter in word:
        if letter not in "a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z":
         return False
    return True

def word_place(spooky_word):
    if 
    
    



print("Welcome to Hangman!")


while True:

    spooky_word = get_random_spooky_word()
    print(f"spooky word is {spooky_word}")
    break

    #guesses_taken = 0
    #while guesses_taken < MAX_WRONG_GUESSES: 
        #guess = ""
        #while len(guess) != len(str(spooky_word)) or not is_only_letters:
            #print(f"Guess #{guesses_taken}: ")
            #guess = input()
        #guesses_taken += 1



pgzrun.go()
