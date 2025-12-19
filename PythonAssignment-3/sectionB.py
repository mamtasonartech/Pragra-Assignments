#Type Casting

#11. Take two strings "10" and "20", convert them into integers, and print their sum.
number_str1 = "10"
number_str2 = "20"
add_numbers = ( int(number_str1) + int(number_str2))
print(add_numbers)

#12. Convert a list of strings ["1", "2", "3"] into a list of integers.
myList = ["1", "2","3"]
#myList_toInteger = [int("1"), int("2"),int("3")]
myList_toInteger=[int(i) for i in myList]
print(myList_toInteger)

#13. Convert the integer 0 into a boolean and print the result.
number_int = 0
integer_to_boolean = bool(number_int)
print(integer_to_boolean)

#14. Convert the float 0.0 into a boolean and print the result.
number_float = 0.0
float_to_bool = bool(number_float)
print(float_to_bool)

#15. Convert a boolean True into an integer and print the output.
boolean_value = True
bool_to_int= int(boolean_value)
print(bool_to_int)

# Dictionaries

#16. Create a dictionary of 3 students with their marks and print the dictionary.

newClass ={
    "student1":{
        "name": "Sanu",
        "marks": 70
    },
    "student2":{
        "name": "Mamta",
        "marks" :90
    },
    "student3":{
        "name": "Ayaan",
        "marks" :80
    }
}
print(newClass)

#17. Check whether a key exists in a dictionary.
print(newClass.keys())

#18. Iterate through a dictionary and print all keys and values.
for key, value in newClass.items():
    print(f"{key} = {value}")

#19. Remove a key from a dictionary.

newClass.pop("student2")
print(newClass)

# 2nd Method
# del newClass["student2"]["marks"]
# print(newClass)

# student2_popped = newClass["student2"].pop("marks",None)
# print(student2_popped)

#20. Count the number of key-value pairs in a dictionary.

count_key_value = len(newClass)
print(count_key_value)

