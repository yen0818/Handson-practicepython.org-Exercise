import random
res_A = [random.randrange(1, 20, 1) for i in range(7)]
res_B = [random.randrange(1, 20, 1) for i in range(12)]
print(res_A, res_B)
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

new = []

for i in res_A:
    for j in res_B:
        if i==j and i not in new:
            new.append(i)

print(new)