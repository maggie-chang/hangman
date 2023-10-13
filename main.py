import pgzrun
import random

max_wrong_guesses = 10


WIDTH = 500
HEIGHT = 300


def draw():
    screen.fill((255, 255, 255))
    spooky_word = get_random_spooky_word()
    print(spooky_word)
    screen.draw.text(spooky_word, (250, 150), color="red")


def get_random_spooky_word():
    with open("words.txt") as file:
        return random.choice(list(file))[:-1]
    
def length_word():
    len(spooky_word)

#def is_only_letters(word):
  



pgzrun.go()
