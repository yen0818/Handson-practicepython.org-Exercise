import datetime

name = input("Please Enter your name: ")
age = input("Please Enter your age: ")

now = datetime.datetime.now()
year = now.year + (100 - int(age))

print(f"Hi, {name}, you will be 100 years old in {year}")



