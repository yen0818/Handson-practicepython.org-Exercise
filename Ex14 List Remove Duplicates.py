def removeDup(n):
    for i in a:
        if i not in new:
            n.append(i)
    return n

def removeDupwithSet(n):
    return list(set(n))

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
new = []
print(removeDup(new))
print(removeDupwithSet(new))