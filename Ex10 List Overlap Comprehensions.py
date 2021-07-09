import random

a = random.sample(range(1,30), 12)
b = random.sample(range(1,30), 16)

# newlist = [j for j in b if j in a and j not in newlist]
newlist=list(dict.fromkeys([k for k in a if k in b]))
print(newlist)