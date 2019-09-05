import random
import os
leftovers = {"a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m", "q", "w", "e", "r", "t", "y", "u", "i", "o", "p"}
fill = []
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
    print("Secret word:", secret_word1)
    print(len(fill))
    return secret_word1
def is_word_guessed(secret_word):
    remains = ""
    for x in fill:
        remains += x
    if(secret_word == remains):
        print("YOU HAVE FILLED OUT THE WORD")
        exit()
    elif(values[1] == 0 and secret_word != remains):
        print("YOU HAVE NO GUESSES REMAINING, YOU LOSE :(\n x.x")
        exit()

def get_guessed_word(secret_word, letters_guessed):
    result = ""
    result2 = ""
    for x in letters_guessed:
        result2 += x
    for x in fill:
        result += x
    print(f"""Guess word so far: {result}\nThese words haven't been used though:{result2}""")
    print(f"""You have a total of {values[1]} incorrect guesses.""")
   #TODO: Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet
def is_guess_in_word(guess, secret_word):
   user_input = guess
   index = 0
   found = False
   verify = True
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
       print(values[1])
       return False
   else:
       for x in leftovers:
           if(x == user_input):
               verify = False
       if(verify == True):
           print("Your guess is in the word! :D")
           leftovers.remove(guess)
           return True
   #TODO: check if the letter guess is in the secret word
def spaceman(secret_word):
   introduction = f"Welcome to spaceman!\nThe secret word contains: {values[0]} letters\n You have a total of {values[1]} incorrect guesses,please enter a letter per round :\n------------------------------------------------------------------------ "
   print(introduction)
   word = ""
   for x in secret_word:
       word += x
   print(len(word))

check = True
#These function calls that will start the game
secret_word = load_word()
print("This is the secret word now:", secret_word)
values = [len(secret_word), 6]

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
       if(values[1]== 6):
           print(phase1)
       elif(values[1]== 5):
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
