#20. Write a function that takes a number and returns whether it is prime.

def check_prime(num20):
        if not isinstance(num20, int):
            return "Invalid input"

        if num20 <= 1:
            return False

        for i in range(2, num20):
            if num20 % i == 0:
                return False

        return True
print(check_prime(7))
print(check_prime(10))

#21. Write a function that takes a number and returns its factorial.

def factorial(num21=None):
    if num21 is None:
        return "Enter numbers. No input receive"
    elif not isinstance(num21, int):
        return "Invalid input: enter an integer"
    elif num21 < 0:
        return "Invalid input: negative numbers not allow"
    elif num21 == 0:
        return 1
    else:
        result = 1
        for i in range(1, num21 + 1):
            result *= i
        return result
print(factorial())
print(factorial(5))
print(factorial(0))
print(factorial(-5))
print(factorial(2.5))

#22. Write a function that takes two numbers and an operator (+, -, *, /) and returns the result.

def calculator(num1 = None, num2 = None, operator = None):
    if None in (num1, num2, operator):
        return "Invalid input,enter all numbers"
    elif not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        return "Invalid input: Please enter valid numbers"
    elif operator not in ["+", "-", "*", "/"]:
        return "Invalid operator"
    elif operator == "/" and num2 == 0:
        return "Cannot divide by zero"
    else:
        if operator == "+":
            return num1 + num2
        elif operator == "-":
            return num1 - num2
        elif operator == "*":
            return num1 * num2
        else:
            return num1 / num2
print(calculator())
print(calculator(10, 5, "+"))
print(calculator(10, 0, "/"))
print(calculator("10", 5, "+"))
print(calculator(10, 5, "%"))

#23. Write a function that takes a number and returns the sum of digits

def sum_of_digits(num23=None):
        if num23 is None:
            return "Enter correct number"
        elif not isinstance(num23, int):
            return "Invalid input: enter an integer"
        elif num23 < 0:
            return "Invalid input: enter a positive number"
        else:
            total = 0
            for digit in str(num23):
                total += int(digit)
            return total

print(sum_of_digits())
print(sum_of_digits(123))
print(sum_of_digits(0))
print(sum_of_digits(-123))
print(sum_of_digits("123"))

#24. Write a function without arguments that returns the largest of three fixed numbers.

def largest_of_three():
    num8 = 12
    num9 = 60
    num10 = 25

    if num8 > num9 and num8 > num10:
        return num8
    elif num9 > num8 and num9 > num10:
        return num9
    else:
        return num10
print(largest_of_three())

#25. Write a function that takes a year and returns whether it is a leap year.

def leap_year(year=None):
    if year is None:
        return "No input receive"
    elif not isinstance(year, int):
        return "Invalid input: enter a valid year"
    elif year <= 0:
        return "Invalid input: year must be positive"
    else:
        # if year % 400 == 0:
        #     return "Its a leap year"
        # elif year % 100 == 0:
        #     return "Its not a leap year"
        # elif year % 4 == 0:
        #     return "Its a leap year"
        if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
            return "It's a leap year"
        else:
            return "It's not a leap year"
print(leap_year(2000))
print(leap_year(2001))

#26. Write a function that takes a number and returns its reverse.

def reverse_number(num26=None):
    if num26 is None:
        return "No input receive"
    else:
        reversed_num = ""
        for n in str(num26):
            reversed_num = n + reversed_num
        return int(reversed_num)
print(reverse_number())
print(reverse_number(12345))

#27. Write a function that takes a string and returns its length without using len().

def string_length(s):
    count = 0
   # for char in s:
    for _ in s:
        count += 1
    return count

print(string_length("Hello"))

#28. Write a function that takes two numbers and returns their LCM.

def lcm(num28 = None , nums28 = None):
    if None in (num28, nums28):
        return "Invalid input"
    elif num28 == 0 or nums28 == 0:
        return "LCM not defined for 0"
    elif num28 > nums28:
        greater = num28
    else:
        greater = nums28

    while True:
        if (greater % num28 == 0) and (greater % nums28 == 0):
            return greater
        greater += 1

print(lcm())
print(lcm(4, 6))
print(lcm(10, 15))
print(lcm(0, 5))

#29. Write a function that takes a number and returns whether it is a palindrome.

def is_palindrome(num29 = None):
    if num29 is None:
        return "Invalid"
    if num29 < 0:
        return "Invalid. Not Palindrome"
    else:
        original = str(num29)
        reverse = original[::-1]

        if original == reverse:
            return "Palindrome"
        else:
            return "Not Palindrome"

print(is_palindrome())
print(is_palindrome(121))
print(is_palindrome(123))

#30. Write a function that takes temperature in Celsius and returns Fahrenheit.

def celsius_to_fahrenheit(celsius=None):
    if celsius is None:
        return "Invalid input. enter a number"
    elif not isinstance(celsius, (int, float)):
        return "Invalid input: Please enter a number not string"
    else:
        fahrenheit = (celsius * 9/5) + 32
        return fahrenheit
print(celsius_to_fahrenheit())
print(celsius_to_fahrenheit(10))
print(celsius_to_fahrenheit(-10))
print(celsius_to_fahrenheit("abc"))

#31. Write a function that takes basic salary and returns net salary after 10% tax.

def net_salary(basic_salary = None):
    if basic_salary is None:
        return "Invalid input: Please enter correct salary"
    elif not isinstance(basic_salary, (int, float)):
        return "Invalid input: Enter a valid number"
    elif basic_salary < 0:
        return "Invalid input: Salary cannot be negative"
    else:
        tax = basic_salary * 10 / 100
        net = basic_salary - tax
        return net

print(net_salary())
print(net_salary("abc"))
print(net_salary(50000))
print(net_salary(-1000))




