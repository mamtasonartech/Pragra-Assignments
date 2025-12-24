# 1.Even or Odd
# Write a program that takes a number as input and checks whether it is even or odd using if and else.

number = int(input("Enter a number: "))
if number % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

# 2. Positive, Negative, or Zero
# Take a number from the user and determine whether it is: ● Positive ● Negative ● Zero
# Use if, elif, and else.

user_input = int(input("Enter any number: "))
if user_input > 0:
    print("The number is positive")
elif user_input < 0:
    print("The number is negative")
else:
    print("The number is zero")

# 3. Voting Eligibility
# Ask the user for their age and check:
# ● If age is 18 or above → eligible to vote ● Otherwise → not eligible

age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")

# 4. Pass or Fail
# Take marks as input and check:  ● If marks are 40 or more, print "Pass" ● Else print "Fail"

student_marks = int(input("Enter your marks: "))
if student_marks >= 40:
    print("Pass")
else:
    print("Fail")

#5. Largest of Two Numbers
# Take two numbers as input and print which number is greater.
# If both are equal, print "Both numbers are equal".

number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

if number1 > number2:
    print("The first number is greater than the second number")
elif number1 < number2:
    print("The second number is greater than the first number")
else:
    print("Both numbers are equal")

