a = [5, 10, 15, 20, 25, 1]

def listEnds():
    return [a[i] for i in range(len(a)) if i==0 or i==len(a)-1]
print(listEnds())