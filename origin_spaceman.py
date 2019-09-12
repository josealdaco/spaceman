import random
import os
from string import punctuation
leftovers = {"a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m", "q", "w", "e", "r", "t", "y", "u", "i", "o", "p"}
fill = []
number_List = set(punctuation)
for x in range(0, 10):
    number_List.add(x)
phase1 = """
        O
        |
      \ | /
        |
       / /
       """
phase2 = """
                O
                |
              \ | /
                |
               /
                """
phase3 = """
                O
                |
              \ | /
                |

                """
phase4 = """
                O
                |
              \ |
                |

                """
phase5 = """
                O
                |
                |
                |

                """
phase6 = """
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
def is_word_guessed(secret_word):
    remains = ""
    for x in fill:
        remains += x
    if(secret_word == remains):
        print("YOU HAVE FILLED OUT THE WORD,HERE IS THE WORD COMPLETED:\n", secret_word)
        exit()

    elif(values[1] == 0 and secret_word != remains):
        print("YOU HAVE NO GUESSES REMAINING, YOU LOSE :(\n x.x, here is the secret word that you missed:", secret_word)
        exit()

def get_guessed_word(secret_word, letters_guessed):
    result = ""
    result2 = ""
    for x in letters_guessed:
        result2 += x
    for x in fill:
        result += x
    print(f"""Guess word so far: {result}\nThese letters haven't been used though:{result2}""")
    print(f"""You have a total of {values[1]} incorrect guesses.""")
   #TODO: Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet
def is_guess_in_word(guess, secret_word):
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
           values[1] -= 1
           print("remaining guesses:", values[1])
           return False
       else:
           for x in leftovers:
               if(x == user_input):
                    verify = False
           if(verify == False):
               print("Your guess is in the word! :D")
               leftovers.remove(user_input)
               return True
           elif(verify == True):
               print("YOUR GUESS HAS ALREADY BEEN USED")
   #TODO: check if the letter guess is in the secret word
def spaceman(secret_word):
   introduction = f"Welcome to spaceman!\nThe secret word contains: {values[0]} letters\n You have a total of {values[1]} incorrect guesses,please enter a letter per round :\n------------------------------------------------------------------------ "
   print(introduction)
   word = ""
   for x in secret_word:
       word += x
   print(len(word))
def validate(x):
    if(x == "RESTARTING"):
        return True
check = True
#These function calls that will start the game
secret_word = load_word()
values = [len(secret_word), 7]

spaceman(secret_word)
while(check):
   x = input("if you want to quit press q, n for new word ,otherwise hit enter to continue:")
   if(x == "q"):
       check = False
       break
   elif(x == "n"):
       secret_word = load_word()
       values[1] = 6
   else:
       os.system('clear')
       if(values[1]== 7):
           print(phase1)
       elif(values[1]== 6):
           print(phase2)
       elif(values[1]== 4):
           print(phase3)
       elif(values[1]== 3):
            print(phase4)
       elif(values[1]== 2):
           print(phase5)
       elif(values[1]== 1):
           print(phase6)
       guess = input("Input letter:")
       is_guess_in_word(guess, secret_word)
       get_guessed_word(secret_word, leftovers)
       is_word_guessed(secret_word)
