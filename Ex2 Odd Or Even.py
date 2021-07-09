num = int(input("Enter a number: "))

if num%2 == 0:
    if num%2 == 0 and num%4 == 0:
        print(f"{num} is a multiple of 4 and it's an Even Number")
    else:
        print(f"{num} is an Even Number")

else:
    print(f"{num} is Odd Number") 
 
check = int(input("Enter a number to divide by: "))

if num%check == 0:
    print(f"{num} can be divides evenly by {check}")
else:
    print(f"{num} does not divides evenly by {check}")