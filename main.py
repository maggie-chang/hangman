import random


def introduction():
    print("""
          Welcome to Hangman!

Instructions and Info:
    - There will be asterisks '*' indicating the # of letters in the word 
        and the corresponding position.
    - For each correct letter guessed, the letter will replace the asterisk, 
        and for each incorrect letter guessed, a body part will be added.
    - The theme of the words will be anything related to the Fall and Spooky season.
          """)
    return True


def get_random_spooky_word():
    with open("words.txt") as file:
        return random.choice(list(file))[:-1].lower()


def is_only_letters(word):
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


def you_lost(spooky_word):
    print("""you lost...
________
| /     |
|            
|
|
|
|
|            
|____+{(x_x)}""")
    print(f"the answer was {spooky_word}")


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
|____+ {x_x} """)


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
    return None


def get_letter_from_player():
    guessed_letter = input("enter a letter: ")

    while (not is_only_letters(guessed_letter)) and len(guessed_letter) == 1:
        print("please enter a single letter")
        guessed_letter = input("enter a letter: ")

    guessed_letter = guessed_letter.lower()
    return guessed_letter


def initial_clue(word):
    result = []
    for _ in word:
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

    while True:

        spooky_word = get_random_spooky_word()
        clue = initial_clue(spooky_word)
        #print(f"DEBUG: spooky word is {spooky_word}")

        max_wrong_guesses = 10
        wrong_guesses_taken = 0

        while wrong_guesses_taken < max_wrong_guesses:
            print(f"""------------------------
you have {wrong_guesses_taken} wrong guess(es) out of 10 taken""")
            print_the_man(num_guesses=wrong_guesses_taken)
            print(clue)

            word_from_player = get_word_from_player()

            if word_from_player is not None:
                if word_from_player == spooky_word:
                    you_win()
                    break
                else:
                    wrong_guesses_taken = wrong_guesses_taken + 1
                    print(f"""
you have #{wrong_guesses_taken} wrong guess(es) taken""")
                    print_the_man(num_guesses=wrong_guesses_taken)

            
            if word_from_player != spooky_word:
                letter_from_player = get_letter_from_player()
                if not update_clue(spooky_word, letter_from_player, clue):
                    wrong_guesses_taken = wrong_guesses_taken + 1

            if wrong_guesses_taken == max_wrong_guesses:
                you_lost(spooky_word)
                break
        break





#############################################################################################
# MAIN PROGRAM
#############################################################################################

introduction()
while True:
    play_hangman()
    print("----------")
    print("do you want to play again? (yes/no)")
    if not input().lower().startswith("y"):
        print("play again sometime soon!")
        break