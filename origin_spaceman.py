import random
import os
from string import punctuation
leftovers = ["a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m", "q", "w", "e", "r", "t", "y", "u", "i", "o", "p"]
fill = []
number_List = set(punctuation)
for x in range(0, 10):
    number_List.add(x)
def character_display(score,max_score):
    """" This function will display character based on current guesses """
    if(score == max_score):
        return """
                O
                |
              \ | /
                |
               / /
               """
    elif(score == max_score - 1):
        return """
                        O
                        |
                      \ | /
                        |
                       /
                        """
    elif(score == max_score -2):
        return """
                        O
                        |
                      \ | /
                        |

                        """
    elif(score == max_score -3):
        return """
                        O
                        |
                      \ |
                        |

                        """
    elif(score == max_score -4):
        return """
                        O
                        |
                        |
                        |

                        """
    elif(score == max_score -5):
        return """
                        O

                        """

def load_word():
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()
    words_list = words_list[0].split(' ')
    secret_word1 = random.choice(words_list)
    fill.clear()
    for x in range(len(secret_word1)):
        fill.append("_")
    print(len(fill))
    return secret_word1
def is_word_guessed(secret_word, values):
    remains = ""
    for x in fill:
        remains += x
    if(secret_word == remains):
        return f"YOU HAVE FILLED OUT THE WORD,HERE IS THE WORD COMPLETED:\n {secret_word} ", exit()

    elif(values[1] == 0 and secret_word != remains):
        return f"YOU HAVE NO GUESSES REMAINING, YOU LOSE :(\n x.x, here is the secret word that you missed: {secret_word}", exit()
    else:
        return "Still in game"

def get_guessed_word(secret_word, letters_guessed,values, fill):
    result = ""
    result2 = ""
    print(letters_guessed)
    for x in letters_guessed:
        result2 += x
        print(x)
    for x in fill:
        result += x
    return f"Guess word so far: {result}\nThese letters haven't been used though:{result2}\n You have a total of {values[1]} incorrect guesses. "
   #TODO: Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet
def is_guess_in_word(guess, secret_word,values):
   user_input = guess
   index = 0
   found = False
   verify = True
   validated = False
   check = False
   while(validated == False):
       if(len(user_input) > 1):
           print("It has to be a single character letter")
           user_input = input("Change answer>>")
       elif(len(user_input) <= 0):
           print("YOU HAVE TO INPUT A LETTER, CAN'T LEAVE IT BLANK")
           user_input = input("Change answer>>")

       for x in number_List:
           for y in user_input:
               if(x == y):
                   print("You cannot have any numbers or symbols as an answer")
                   user_input = input("Change Response>>")
       if(len(user_input) == 1):
           print("checking input")
           for x in user_input:
               for y in number_List:
                   if(y != x):
                       check = True
                   elif(y == x):
                       check = False
           if(check == True):
               print("breacking")
               validated = True
               break
   if validated is True:
       print("This is the rest list:", fill)
       for x in secret_word:
           if(x == user_input):
               print("Letters found")
               fill[index] = user_input
               found = True
           index += 1
       if(found is False):
           print("LETTER INCORRECT")
           try:       # this will
               leftovers.remove(user_input)
               values[1] -= 1
           except:
               print("Guess has already been removed")
           print("remaining guesses:", values[1])
           return False
       else:
           for x in leftovers:
               if(x == user_input):
                    verify = False
           if(verify == False):
               print("Your guess is in the word! :D")
               try:
                   leftovers.remove(user_input)
               except:
                   print("Guess has already been removed")
               return True
           elif(verify == True):
               print("YOUR GUESS HAS ALREADY BEEN USED")
   #TODO: check if the letter guess is in the secret word
def spaceman(secret_word, values):
   introduction = f"Welcome to spaceman!\nThe secret word contains: {values[0]} letters\n You have a total of {values[1]} incorrect guesses,please enter a letter per round :\n------------------------------------------------------------------------ "
   print(introduction)
   word = ""
   for x in secret_word:
       word += x
   print(len(word))
def program_run():
    check = True
    #These function calls that will start the game
    secret_word = load_word()
    values = [len(secret_word), 7]
    spaceman(secret_word, values)
    while(check):
       x = input("if you want to quit press q, n for new word ,otherwise hit enter to continue:")
       if(x == "q"):
           check = False
           break
       elif(x == "n"):
           secret_word = load_word()
           values[1] = 7
       else:
           os.system('clear')
           print(character_display(values[1],7))
           guess = input("Input letter:")
           is_guess_in_word(guess, secret_word, values)
           print(get_guessed_word(secret_word, leftovers, values, fill))
           print(is_word_guessed(secret_word, values))




    print(get_guessed_word("max", leftovers, values, fill))
if __name__ == "__main__":
    program_run() # Runs the function if called upon
