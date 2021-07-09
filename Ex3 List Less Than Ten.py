a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
newa = [i for i in a if i<5]
ele = int(input("Input a number: "))
print([i for i in a if i<ele])
