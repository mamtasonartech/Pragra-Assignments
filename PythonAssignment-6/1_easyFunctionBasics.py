#1. Write a function without arguments that prints "Learning Python Functions".

def printText():
    print("Learning Python Functions")
printText()

#2. Write a function without arguments that prints numbers from 1 to 5.

def printNumbers():
    for num in range(1,6):
        print(num)
printNumbers()

#3. Write a function with one argument that prints the value passed.

def greet_user(username):
    if not username:
        print("Hello, Guest!")
    elif not isinstance(username, str):
        print("Invalid username")
    else:
        print(f"Hello, {username}")
greet_user("Mamta")

#4. Write a function with two arguments that prints their sum.

def sumNumbers(number1=None, number2=None):
    if number1 is None or number2 is None:
        print("Invalid input,both numbers are required")
    else:
        add= number1 + number2
        print(add)
sumNumbers(2,4)

#5. Write a function without arguments that prints today’s greeting message.

def todays_greeting():
    print("Hello , Have a wonderful day?")
todays_greeting()

#6. Write a function that takes a name as an argument and prints "Hello <name>".

def myName(name):
    if not name:
        print("Hello, Guest!")
    elif not isinstance(name, str):
        print("Invalid name")
    else:
        print(f"Hello,{name}")

myName("Mamta")

#7. Write a function without arguments that prints the square of 5.

def square_num():
    nums = 5
    square_of = nums * nums
    print(square_of)
square_num()

#8. Write a function with one argument that prints whether the number is positive.

def check_num(number=None):
    if number is None or number == "":
        print("Invalid number")
    elif number > 0:
        print("Number is positive")
    elif number < 0:
        print("Number is negative")
    else:
        print("Number is zero")
check_num()
check_num(0)
check_num(1)
check_num(-1)