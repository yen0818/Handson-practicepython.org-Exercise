def ver1():
    mylist = [i for i in string_input.split(" ")]
    reverselist = []
    for i in range(len(mylist)):
        reverselist.append(mylist[-1])
        mylist.pop()
    return " ".join(reverselist)

def ver2():
    a = string_input.split()
    return " ".join(a[::-1])

def ver3_shorterver2():
    return " ".join([i for i in string_input.split()[::-1]])

string_input = input("Insert a string: ")
print(ver1())
print(ver2())
print(ver3_shorterver2())

