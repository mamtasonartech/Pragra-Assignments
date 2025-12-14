#1. Create a string variable with your name and print it.
myName = "Mamta"
print(myName)

#2. Store a string "Python" and print its length.
programmingLang ="Python"
print(len(programmingLang))

#3. Create two string variables and join them using the + operator.
myCity = "Orillia"
myProvince ="Ontario"
print(myCity + " " + myProvince)

#4. Store a word and print it 3 times using an operator.
myFavColor = "Purple"
print(myFavColor * 3)

#5. Given a string "Hello World", print only "Hello".
str1= "Hello World"
print(str1[:5])
print(str1.split()[0])

#6. Create a string and print its first and last character.
str2= "Sonar"
print(str2[0])
#or
print (str2[4])

#7. Check whether the word "Python" exists in the string "I am learning Python".
str3 = "I am learning Python"
print("Python" in str3)

#8. Store a string with extra spaces at the beginning and end and remove the spaces.
str4 = " Python "
print(str4.strip())

#9. Convert the string "python" to uppercase.
str5 = "Python"
print(str5.upper())

#10. Count how many times the letter "a" appears in "banana".
str6 = "banana"
print(str6.count("a"))