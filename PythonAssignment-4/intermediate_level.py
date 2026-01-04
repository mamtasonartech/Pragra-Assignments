# 6. Grade Calculator
# Take marks as input and assign grades:
# ● 90 and above → Grade A ● 75 to 89 → Grade B ● 50 to 74 → Grade C ● Below 50 → Fail

marks = int(input("Enter your marks: "))
if marks >= 90:
    print("Grade A")
elif 75 <= marks <= 89:
    print("Grade B")
elif 50 <= marks <= 74:
    print("Grade C")
else:
    print("Fail")

# 7. Simple Calculator (Conditions Only)
# Take two numbers and an operator (+, -, *, /) as input.
# Use if-elif-else to perform the correct operation.

number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
operation = input("Which operation would you like to perform? (+,-,*,/): ")
if operation == "+":
    print(number1 + number2)
elif operation == "-":
    print(number1 - number2)
elif operation == "*":
    print(number1 * number2)
elif operation == "/":
    print(number1 / number2)
else:
    print("You entered the invalid operator")

# 8. Temperature Check
# Take temperature in Celsius and print: ● "Cold" if temperature < 15
# ● "Moderate" if temperature is between 15 and 30 ● "Hot" if temperature > 30

temperature = float(input("Enter temperature in Celsius: "))
if temperature < 15:
    print("Cold")
elif 15 <= temperature <= 30:
    print("Moderate")
else:
    print("Hot")

# 9. Login Validation
# Take a username and password as input.
# ● If both match predefined values, print "Login successful" ● Else print "Invalid credentials"

user_name = input("Enter your user name: ")
password = input("Enter your password: ")

if user_name == "admin" and password == "admin":
    print("Login successful")
else:
    print("Invalid credentials")

# 10. Electricity Bill Slab
# Take the number of units consumed and calculate the bill:
# ● Up to 100 units → ₹5 per unit ● 101–200 units → ₹7 per unit ● Above 200 units → ₹10 per unit
# Use if, elif, and else.

user_units = int(input("Enter Units consumed: "))
if user_units <= 100:
    bill = 5 * user_units
elif 101 <= user_units <=200:
    bill = 7 * user_units
else:
    bill = 10 * user_units

print("Your total bill is : "  + str(bill))


