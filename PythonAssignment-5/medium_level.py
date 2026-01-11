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