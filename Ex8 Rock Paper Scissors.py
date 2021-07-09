import sys

def rules(p1,p2):
    if (p1=='R' and p2=='S') or (p1=='S' and p2=='P') or (p1=='P' and p2=='R'):
        print("Congratulations Player 1")
    elif (p2=='R' and p1=='S') or (p2=='S' and p1=='P') or (p2=='P' and p1=='R'):
        print("Congratulations Player 2")
    elif (p2=='R' and p1=='R') or (p2=='P' and p1=='P') or (p2=='S' and p1=='S'):
        print("Its a tie")
    else:
        print("Invalid Input")
        sys.exit()

while True:
    p1 = input("Player 1 Rock Paper Scissors: R/P/S ")
    p2 = input("Player 2 Rock Paper Scissors: R/P/S ")
    rules(p1,p2)

    newgame = input("Start Next Round? y/n ")
    if newgame == 'y':
        continue
    else:
        break