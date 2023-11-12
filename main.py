# import pgzrun
import random

max_wrong_guesses = 10


def introduction():
    print(
        """
          Welcome to Hangman!

Instructions and Info:
    -  All words are anything related to the fall season
    - There will be asterisks '*' indicating the # of letters in the word
    - For each incorrect letter guessed, a body part will be added
          """
    )
    return True


def get_random_spooky_word():
    """returns a random word from words.txt"""
    with open("words.txt") as file:
        return random.choice(list(file))[:-1].lower()


def is_only_letters(word):
    """makes sure players' input is only letters"""
    for letter in word:
        if (
            letter
            not in "a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z"
        ):
            return False
    return True


def you_win():
    return print(
        """
________
| /     |
|
|   
|      (:D)
|      \ | /
|        | 
|        |
|____+  / \ 
you saved the man!"""
    )


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
|____+ """)
        
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
|____+ """)
        
    if num_guesses == 2:
        print("""
________
| /     |
|     (:D)
|       |
|       |
|       |
|
|
|____+ """)
        
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
|____+ """)
        
    if num_guesses == 4:
        print(
            """
________
| /     |
|      (:/)
|        | 
|      / | \ 
|        |
|
|
|____+ """)
        
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
|____+ """)
        
    if num_guesses == 6:
        print(
            """
________
| /     |
|     (-_-)
|       | 
|     / | \ 
|       |
|      / \ 
|
|____+ """)
        
    if num_guesses == 7:
        print(
            """
________
| /     |
|     (x_x)
|
|       | 
|     / | \ 
|       |
|      / \ 
|____+  """)
        
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
|____+{___} """)
        
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
|____+{___} """)

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
|____+{(0_0)}""")


def get_word_from_player():
    spooky_word = get_random_spooky_word()
    wants_word_guess = ""

    while wants_word_guess != "yes" and wants_word_guess != "no":
        wants_word_guess = input("would you like to guess the word? (yes/no): ")
        wants_word_guess = wants_word_guess.lower()

    if wants_word_guess == "yes":
        guessed_word = input("enter a word: ")

        while not is_only_letters(guessed_word):
            print("please use only letters")
            guessed_word = input("enter a word: ")

        guessed_word = guessed_word.lower()
        return guessed_word
    return ""


def get_letter_from_player():
    guessed_letter = input("enter a letter: ")

    while (not is_only_letters(guessed_letter)) and len(guessed_letter) == 1:
        print("please enter a single letter")
        guessed_letter = input("enter a letter: ")

    guessed_letter = guessed_letter.lower()
    return guessed_letter


def initial_clue(str):
    result = []
    for _ in str:
        result.append("*")
    return result


def index_of_letter_in_word(char, spooky_word):
    index = 0
    for letter in spooky_word:
        if letter == char:
            return index
        index = index + 1

    return -1


def update_clue(word, letter, clue):
    letter_index = index_of_letter_in_word(letter, word)
    if letter_index != -1:
        clue[letter_index] = letter
        return True
    else:
        return False


def play_hangman():
    introduction()

    while True:
        spooky_word = get_random_spooky_word()
        clue = initial_clue(spooky_word)
        print(f"DEBUG: spooky word is {spooky_word}")

        wrong_guesses_taken = 0

        while wrong_guesses_taken < max_wrong_guesses:
            print(f"you have #{wrong_guesses_taken} wrong guess(es) taken")
            print_the_man(num_guesses=wrong_guesses_taken)
            print(clue)

            word_from_player = get_word_from_player()

            if word_from_player == spooky_word:
                you_win()
                break
            else:

                letter_from_player = get_letter_from_player()
                if not update_clue(spooky_word, letter_from_player, clue):
                    wrong_guesses_taken = wrong_guesses_taken + 1

        break


#############################################################################################
# MAIN PROGRAM
#############################################################################################

# introduction()
play_hangman()
# pgzrun.go()