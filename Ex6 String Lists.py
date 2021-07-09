stringinput = input("Input a string: ")
print(stringinput[-1]) # Notes: string to element

rvs=stringinput[::-1]
if stringinput == rvs : # or if stringinput[::] == stringinput[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

def reverse(stringinput):
    x = ''
    for i in range(len(stringinput)):
        x += stringinput[len(stringinput)-1-i]
    return x
if stringinput == reverse(stringinput) :
    print("(For Loop) Palindrome")
else:
    print("(For Loop) Not Palindrome")