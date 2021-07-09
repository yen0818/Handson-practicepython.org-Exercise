import random
import sys

def guess(num, guess_num, n):
    if num>guess_num :
        print("Your guess is too low")
    elif num<guess_num :
        print("Your guess is too high")
    else:
        print("You're correct") 
        printnumguess(n) 
        startnewgame = input("Start New Game? y/n ")
        if startnewgame == 'y':
            newgame()
        else:
            sys.exit()

def printnumguess(n):
    print(f"You guessed {n} times")

def newgame():

    num = random.randint(0,9)
    n=1
    while True:
        guess_num = input("Guess a Number/ exit: ")
        if guess_num == 'exit':
            sys.exit()
        elif guess_num.isnumeric(): 
            guess(num, int(guess_num), n)
            n+=1
        else:
            print("Invalid Input!")

newgame()
   

    