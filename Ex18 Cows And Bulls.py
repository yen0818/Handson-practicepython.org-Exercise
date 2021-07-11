import random

benchmark = [random.randint(1,9) for i in range(4)]
print(benchmark)

while True:
    cow = 0
    bull = 0
    count = 0
    digits = input("Input a 4 digit-num: ")

    for i in [int(x) for x in str(digits)]:
        if i in benchmark:
            if i == benchmark[count]:
                cow+=1
                benchmark.remove(i)
            else:
                bull+=1
        count+=1
    print(cow, bull)
    if(cow==4):
        break
    
print("You're Just Right! It's ",benchmark)