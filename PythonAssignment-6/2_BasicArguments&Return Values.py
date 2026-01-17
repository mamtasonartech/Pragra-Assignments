# 9. Write a function that takes two numbers and returns their difference.

def num_diff(number1 =None, number2=None):

    if not isinstance(number1, (int, float)) or not isinstance(number2, (int, float)):
        return "Invalid input"
    else:
        num_minus = number1 - number2
        return num_minus
print(num_diff(24,4))

# 10. Write a function without arguments that returns your age.

def my_age():
     age = 36
     return age
print(f"My age is {my_age()}")

# 11. Write a function that takes a number and returns its square.

def square_num(number3=None):
    if number3 is None or number3 == "":
        return "Invalid number"
    else:
        square_res= number3 * number3
        return square_res
print(square_num())
print(square_num(5))

#12. Write a function that takes two arguments and returns the larger number.

def large_num(number4=None,number5=None):
    if number4 is None or number5 is None:
        return "Invalid input,both numbers are required"
    elif number4 > number5:
        return f"{number4} is greater than {number5}"
    elif number4 < number5:
        return f"{number5} is greater than {number4}"
    else:
        return "Both are equal"
print(large_num())
print(large_num(20))
print(large_num(25,45))
print(large_num(25,25))

#13. Write a function without arguments that returns the value 100.

def val_return():
    return 100
print(val_return())

#14. Write a function that takes a number and returns "Even" or "Odd".

def evenodd(number6=None):
    if number6 is None:
        return "Invalid Input"
    elif number6%2 == 0:
        return "Number is even"
    else:
        return "Number is odd"

print(evenodd())
print(evenodd(2))

#15. Write a function that takes length and breadth and returns the area of a rectangle.

def area_rectangle(length = None,breadth=None):
    if length is None or breadth is None:
        return "Invalid input,enter length and breadth"
    elif length < 0 or breadth < 0:
       return "Invalid Dimensions"
    else:
        area = length * breadth
        return area
print(area_rectangle(4,8))

#16. Write a function without arguments that returns the sum of two fixed numbers.

def sum_fixed_number():
    num1 = 10
    num2 =20
    return num1 + num2
print(sum_fixed_number())

#17. Write a function that takes marks as an argument and returns "Pass" or "Fail".

def stu_results(marks):
    if not isinstance(marks, (int, float)) or marks < 0 or marks > 100:
        return "Invalid marks"
    elif  marks >= 40:
        return "Pass"
    else:
        return "Fail"
print(stu_results(40))

#18. Write a function that accepts three numbers and returns their average.

def average_numbers(num4=None,num5=None,num6=None):
    if None in (num4, num5, num6):
        return "Invalid input,enter all numbers"
    elif not isinstance(num4, (int, float)) or not isinstance(num5, (int, float)) \
            or not isinstance(num6, (int, float)):
        return "Invalid input, numbers only"
    else:
        return (num4 + num5 +num6) /3
print(average_numbers(10,20,30))
print(average_numbers())
print(average_numbers("A","B","C"))

#19. Write a function without arguments that prints a menu message.

def food_menu():
    print("""
------ FOOD MENU ------
1. Pizza
2. Burger
3. Pasta
4. Fries
5. Taco
6. Exit
""")

food_menu()





