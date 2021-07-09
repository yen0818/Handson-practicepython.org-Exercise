n = int(input("Enter how many Fibonnaci: "))

def Fibo(n):
    
    if n==0:
        fibolist = []
    elif n==1:
        fibolist = [1]
    elif n==2:
        fibolist = [1,1]
    elif n>2:
        fibolist = [1,1]
        for i in range(n-2):
            fibolist.append(fibolist[-1]+fibolist[-2])
    return fibolist

print(Fibo(n))

