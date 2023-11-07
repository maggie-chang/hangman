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
        if (letter not in "a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z"):
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
    

    
def print_the_man(num_guesses):

    if num_guesses == 0:
        print("""
________
| /     |
|
|
|
|
|
|
|____+
""")
                
    if num_guesses == 1:
        print("""
________
| /     |
|     (:D)
|
|
|
|
|
|____+
""")        
    if num_guesses  == 2:
        print("""
________
| /     |
|     (:D)
|       |
|       |
|       |
|
|
|____+
""")                           
    if num_guesses == 3:
        print("""
________
| /     |
|     (:D)
|     \ | 
|       |
|       |
|
|
|____+

""")              
    if num_guesses == 4:
        print("""
________
| /     |
|      (:/)
|        | 
|      / | \
|        |
|
|
|____+

""")        
    if num_guesses == 5:
        print("""
________
| /     |
|     (._.)
|       | 
|     / | \
|       |
|      / 
|
|____+

""")        
    if num_guesses == 6:
        print("""
________
| /     |
|     (-_-)
|       | 
|     / | \
|       |
|      / \
|
|____+
""")        
    if num_guesses == 7:
        print("""
________
| /     |
|     (x_x)
|
|       | 
|     / | \
|       |
|      / \
|____+  

""")        
    if num_guesses == 8:
        print("""
________
| /     |
|     (x_x)
|
|
|
|
|              
|____+{___}
""")        
    if num_guesses == 9:
        print("""
________
| /     |
|            
|
|     (x_x)
|
|
|              
|____+{___}
""")

    if num_guesses == 10:
        print("""
________
| /     |
|            
|
|     
|
|
|              
|____+{(0_0)}
""")



def clues_from_letter(spooky_word: str, guessed_letter):
    clue = ""
    guess_index = spooky_word.index(guessed_letter)

    for i in range(len(spooky_word)):
        if i == guess_index:
            clue += guessed_letter
        else:
            clue += "*"

    return clue



def initial_clue(str):
    """edit this so it takes the guess and returns a new string but with the correctly guessed letter"""
    result = []
    for _ in str:
        result.append("*")
    return result



def get_word_from_player():
    guessed_word = input("enter a word: ")
    
    while not is_only_letters(guessed_word):
        print("please use only letters")
        guessed_word = input("enter a word: ")

    guessed_word = guessed_word.lower()
    return guessed_word



def get_letter_from_player():
    guessed_letter = input("enter a letter: ")
    
    while (not is_only_letters(guessed_letter)) and len(guessed_letter) == 1:
        print("please enter a single letter")
        guessed_letter = input("enter a letter: ")

    guessed_letter = guessed_letter.lower()
    return guessed_letter



def index_of_letter_in_word(letter, word):
    word = get_random_spooky_word
    word_index = letter.index(word)



def play_hangman():

    while True:
        spooky_word = get_random_spooky_word()
        clue = initial_clue(spooky_word)
        print(f"DEBUG: spooky word is {spooky_word}")

        wrong_guesses_taken = 0
        
        while wrong_guesses_taken < max_wrong_guesses:
            #print(clues_from_letter(guess, spooky_word))
            print(clue)

            # ensure all letters
            while wrong_guesses_taken != max_wrong_guesses or not is_only_letters(guess):
                print(f"you have {wrong_guesses_taken} wrong guess(es) taken")

            # check if letter is in word
            if guess in spooky_word:
                pass

            wrong_guesses_taken += 1


        while wrong_guesses_taken == max_wrong_guesses:
            word_guess = input("This is your last attempt. Make a *word* guess: ")

            # if the letter the player inputs is not in the word, returns *
            if word_guess == correct_word:
                break
            elif wrong_guesses_taken > max_wrong_guesses:
                print(f"""you lost...

    the answer was {spooky_word}""")
            break



#############################################################################################
# MAIN PROGRAM
#############################################################################################
introduction()
play_hangman()
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
