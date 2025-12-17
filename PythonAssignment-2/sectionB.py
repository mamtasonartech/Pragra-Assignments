#11. Given a string "Python Programming", print "Programming" using slicing.
str11 = "Python Programming"
print(str11[7:18])

#12. Store a string and check whether it starts with "Py".
str12 = "Python"
print(str12.startswith("Py"))

strex12 = "Java"
print(strex12.startswith("Py"))

#13. Store a string and check whether it ends with ".py".
str13 = "myPythonProject.py"
print(str13.endswith(".py"))

strex13 = "myJavaProject.c"
print(strex13.endswith(".py"))

#14. Replace "Java" with "Python" in the string "I like Java".
str14 = "I like Java"
print(str14.replace("Java", "Python"))

#15. Split the string "apple,banana,orange" into a list.
str15 = "apple,banana,orange"
print(str15.split(","))

#16. Join the list ["I", "love", "Python"] into a single string.
str16 = ["I", "love", "Python"]
print(" ".join(str16))

#17. Find the index of "data" in the string "big data engineering".
str17 = "big data engineering"
x= str17.index("data")
print(x)

#18. Compare two strings and print True if they are equal.
a = "I like Python"
b = "I like Python"

if a == b:
    print("True")
else:
    print("False")

#19. Use logical operators to check if a number is greater than 10 and less than 50.

p = int(input("Enter a number: "))
#print(p > 10 and p < 50)
if p > 10 and p < 50:
    print("True")
else:
    print("False")

#20. Use arithmetic operators to calculate the result of (20 + 10) * 2.
res = (20 + 10) * 2
print(res)
