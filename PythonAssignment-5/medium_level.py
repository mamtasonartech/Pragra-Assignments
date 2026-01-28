#18. Write a program to count how many even and odd numbers are present in a list.
odd_even_list=[11,12,13,14,15,16,17]

if not odd_even_list:
    print("The list is empty")
else:
    eve = 0
    odd = 0
    for num in odd_even_list:
        if num % 2 == 0:
            eve += 1
        else:
            odd += 1

    print("Even numbers: ",eve)
    print("Odd numbers: ",odd)

#19. Write a program to remove all negative numbers from a list (print only positive numbers).

numbers = [21, -23, 55, 99, -47, 28]
if not numbers:
    print("The list is empty")
else:

    positive = []
    for nums in numbers:
        if nums > 0:
            positive.append(nums)
    print(positive)


#20. Given a list of numbers, stop printing elements when a number greater than 50 is found.

number_list = [21, 23, 45, 99, 47, 28]
if not number_list:
    print("The list is empty")
else:
    for num1 in number_list:
        if num1 > 50:
            break
        print(num1)

#21. Write a program to reverse a list using a while loop.

number_reverse = [1, 2, 3, 4, 5]

if not number_reverse:
    print("The list is empty")
else:
    reversed_list = []
    i = len(number_reverse) - 1
    while i >= 0:
        reversed_list.append(number_reverse[i])
        i -= 1

    print(reversed_list)

# 22. Write a program to find the second largest number in a list.

second_largest = [21, 23, 45, 99, 47, 28]
if not second_largest:
    print("The list is empty")
elif len(second_largest) < 2:
    print("Second largest does not exist")
else:
    second_largest.sort(reverse=True)
    print(second_largest[1])

# 23. Write a program to print duplicate elements from a list.

find_duplicate = [1, 2, 3, 4, 5, 2 , 6, 4]
if not find_duplicate:
    print("The list is empty")
else:
    duplicates = [i for i in set(find_duplicate) if find_duplicate.count(i) > 1]
    if duplicates:
        print("Duplicate elements:", duplicates)
    else:
        print("No duplicates found")


# 24. Write a program that takes user input repeatedly and stores values in a list until the user enters -1.

# myList = []
# user_input = int(input("Enter the number of elements: "))
# for i in range(user_input):
#     element = input(f"Enter element {i+1}: ")
#     myList.append(element)
#
# print("List:", myList) #not sure how to ADD -1 condition


numbers_list = []
while True:
    num = int(input("Enter a number: "))
    if num == -1:
        break
    numbers_list.append(num)

print("You entered:", numbers_list)

# 25. Write a program to check whether a list is sorted in ascending order or not.

check_ascending = [1,2,3,4]

if not check_ascending:
    print("The list is empty")
elif len(check_ascending) < 2:
        print("list has one element")
else:
    result = True
    for i in range(len(check_ascending) - 1):
        if check_ascending[i] > check_ascending[i + 1]:
            result = False
            break
    print(result)