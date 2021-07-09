num = int(input("Enter a number to get divisors: "))
mylist=[]
for i in range(1, num+1):
    if num%i == 0:
        mylist.append(i)
print(mylist)