import random
leftovers = {"a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m", "q", "w", "e", "r", "t", "y", "u", "i", "o", "p"}
fill = []
def load_word():

    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()

    words_list = words_list[0].split(' ')
    secret_word = random.choice(words_list)
    for x in range(0, len(secret_word)):
        fill.append("_")
    return secret_word

def is_word_guessed(secret_word, letters_guessed):


    return False

def get_guessed_word(secret_word, letters_guessed):
    result = ""
    result2 = ""
    for x in letters_guessed:
        result2 += x
    for x in fill:
        result += x
    print(f"""Your guess is in the word!\nGuess word so far: {result}\nThese words haven't been used though:{result2}""")

    #TODO: Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet


def is_guess_in_word(guess, secret_word):
    user_input = guess
    index = 0
    found = False
    for x in secret_word:
        if(x == user_input):
            print("Letters found")
            fill[index] = user_input
            found = True
        index += 1
    if(found is False):
        print("LETTER INCORRECT")
        values[1] -= 1
        print(values[1])
        return False
    else:
        return True

    #TODO: check if the letter guess is in the secret word






def spaceman(secret_word):
    values = [len(secret_word), 7]
    introduction = f"Welcome to spaceman!\nThe secret word contains: {values[0]} letters\n You have a total of {values[1]} incorrect guesses,please enter a letter per round :\n------------------------------------------------------------------------ "
    print(introduction)
    word = ""
    for x in fill:
        word += x
    print(word)


    #TODO: show the player information about the game according to the project spec

    #TODO: Ask the player to guess one letter per round and check that it is only one letter

    #TODO: Check if the guessed letter is in the secret or not and give the player feedback

    #TODO: show the guessed word so far

    #TODO: check if the game has been won or lost






#These function calls that will start the game
secret_word = load_word()
spaceman(load_word())
guess = input("Input letter:")
is_guess_in_word(guess, secret_word)
get_guessed_word(secret_word, leftovers)
