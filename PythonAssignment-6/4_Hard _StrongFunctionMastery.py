#32. Write a function that takes marks and returns grade (A, B, C, Fail) based on conditions.
def grade(marks=None):

    if marks is None:
        return "Invalid input: marks missing"
    elif not isinstance(marks, (int, float)):
        return "Invalid input: enter a valid number"
    elif marks < 0 or marks > 100:
        return "Invalid input: marks must be between 0 and 100"
    else:
        if marks >= 90:
            return "A"
        elif marks >= 70:
            return "B"
        elif marks >= 45:
            return "C"
        else:
            return "Fail"

print(grade())
print(grade("abc"))
print(grade(120))
print(grade(95))
print(grade(85))
print(grade(65))
print(grade(40))

#33. Write a function that takes three numbers and returns the second largest number.

def second_largest(num1=None, num2=None, num3=None):
    if None in (num1, num2, num3):
        return "Invalid input: enter all three numbers"
    else:
        nums = [num1, num2, num3]
        nums.sort()
        return nums[-2]

print(second_largest())
print(second_largest(10, 20, 30))
print(second_largest(30, 15, 10))

#34. Write a function that takes a number and returns both count of digits and sum of digits.

def digits_info(num34=None):
    if num34 is None:
        return "Invalid input: Please enter a number"
    elif not isinstance(num34, int):
        return "Invalid input: Enter an integer number"
    else:
        num34 = abs(num34)
        count = 0
        total = 0

        while num34 > 0:
            digit = num34 % 10
            total += digit
            count += 1
            num34 //= 10
        return count, total

print(digits_info())
print(digits_info(12345))
print(digits_info(-789))

#35. Write a function that takes two numbers and returns their HCF using logic (not built-in).
def hcf(num35=None, nums35=None):

    if num35 is None or nums35 is None:
        return "Invalid input: enter both numbers"
    elif not isinstance(num35, int) or not isinstance(nums35, int):
        return "Invalid input: numbers only"

    num35 = abs(num35)
    nums35 = abs(nums35)
    if num35 == 0 or nums35 == 0:
        return "HCF not defined for 0"

    smaller = num35 if num35 < num35 else nums35

    while smaller > 0:
        if num35 % smaller == 0 and nums35 % smaller == 0:
            return smaller
        smaller -= 1

print(hcf())
print(hcf(4, 26))
print(hcf(12, 18))
print(hcf(7, 5))

