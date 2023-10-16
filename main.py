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
    with open("words.txt") as file:
        return random.choice(list(file))[:-1]
  

def is_only_letters(word):
    for letter in word:
        if letter not in "a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z":
         return False
    return True

def word_place(spooky_word):
    spooky_word = get_random_spooky_word
    if len(spooky_word) != 

    
    



print("this is hanging!")


while True:


    spooky_word = get_random_spooky_word(num_letters)
    print(f"spooky word is {spooky_word}")

    num_letters = len(spooky_word)

    while len(spooky_word) != int(num_letters):
        new_spooky_word = get_random_spooky_word()
        print(f"new spooky word is {spooky_word}")
        break

    wrong_guesses_taken = 0
    while wrong_guesses_taken < max_wrong_guesses:
        guess = ""



pgzrun.go()
