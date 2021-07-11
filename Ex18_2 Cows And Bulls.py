import random
from collections import Counter

userGuess = ''
randNum = ''
dicRan = {}


for i in range(0, 4):
    rNum = str(random.randint(0, 9))
    randNum += rNum

for x in range(0, 4):
    dicRan[randNum[x]] = list(randNum).count(randNum[x])  

print('Welcome to the Cows and Bulls Game!')
print(randNum)

while userGuess != randNum:
    while len(userGuess) != 4 or str(userGuess).isdecimal() == False:
        userGuess = str(input('Enter a four digit number: '))

    cow = 0
    bull = 0
    dicUser = {}
    dicBull = {}
    dicCow = {}

    for x in range(0, 4):
        dicUser[userGuess[x]] = list(userGuess).count(userGuess[x])

    for i in range(0, 4):
        if randNum[i] == userGuess[i]:
            dicCow[randNum[i]] = dicCow.get(randNum[i], 0) + 1

    for i in dicCow:
         cow += dicCow[i]

    dicCow = Counter(dicCow)
    dicRan = Counter(dicRan)
    dicBull = dicRan - dicCow

    for t in dicUser:
        if t in dicBull:
            bull += dicBull[t]


    print('Wrong guess. Cows: {} Bulls: {}'.format(cow, bull))
    userGuess = str(input('Try again: '))

if userGuess == randNum:
    print('You guessed correctly!')