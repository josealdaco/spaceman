#Variable below
values = [4, 7] ## initial values
rounds = True
word = "jackass"
fill = ["_", "_", "_", "_", "_", "_", "_"]
leftovers = {"a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m", "q", "w", "e", "r", "t", "y", "u", "i", "o", "p"}

#Functions below
def intro():
    introduction = f"Welcome to spaceman!\nThe secret word contains: {values[0]} letters\n You have a total of {values[1]} incorrect guesses,please enter a letter per round :\n------------------------------------------------------------------------ "
    print(introduction)
    word = ""
    for x in fill:
        word += x
    print(word)
def game():
    user_input = input("Input letter:")
    result = ""
    result2 = ""
    print(leftovers)
    index = 0
    found = False
    for x in word:
        if(x == user_input):
            print("Letters found")
            fill[index] = user_input
            found = True
        index += 1
    if(found is False):
        print("LETTER INCORRECT")
        values[1] -= 1
        print(values[1])
    else:
        leftovers.remove(user_input)
        for x in leftovers:
            result2 += x
        for x in fill:
            result += x
        print(f"""Your guess is in the word!\nGuess word so far: {result}\nThese words haven't been used though:{result2}""")


intro()
while(rounds):
    response = input("IF YOU EVER WANT TO QUIT PRESS THE Q BUTTON")
    if(response == "Q"):
        rounds = False
        break
    game()
