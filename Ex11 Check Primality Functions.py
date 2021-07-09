num = int(input("Input a number: "))
mylist = [ i for i in range(2, num) if num % i ==0]

def isPrime(mylist):
    if num>1:
        if len(mylist) == 0:
            return True
        else:
            return False
    else:
        return False

if isPrime(mylist):
    print("PRIME")
else:
    print("NOT PRIME")