# The exercise can be found at: http://www.practicepython.org/exercise/2014/11/11/20-element-search.html
#
# Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to largest) 
# and another number. The function decides whether or not the given number is inside the list and returns (then prints) 
# an appropriate boolean.

# find is a function that takes an ordered list of numbers and another number,
# returning true or false whether the element appears in the list
# 
# l is a list ordered from smallest to largest
# element is the number to find in the original list

# normal search
def findEle(l,ele):
    if ele in l:
        return True
    else:
        return False

def BinarySearch(l, ele):
    start_index = 0
    end_index = len(l) - 1
    while True:
        middle_index = int((end_index + start_index) / 2)
        middle_ele = l[middle_index]

        if middle_ele == ele or l[start_index] == ele or l[end_index] == ele:
            return True
            break

        if middle_index == start_index or middle_index == end_index or middle_index == 0:
            return False
            break

        elif middle_ele > ele:
            end_index = middle_index

        else:
            start_index = middle_index

mylist = [1, 2, 3, 4, 5, 10]
print(findEle(mylist, 4))
print(findEle(mylist, 10))
print(BinarySearch(mylist, 4))
print(BinarySearch(mylist, 10))

