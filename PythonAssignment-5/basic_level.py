#9. Write a program to print all elements of a list until a value 0 is found, using break.

myList= [1,2,35,4,56,0,98,6,5,10]

for list_item in myList:
    if list_item == 0:
        break
    print(list_item)

#10. Write a program to count how many elements are in a list using a while loop.

colors = ['red', 'green', 'blue', 'yellow', 'orange', 'cyan']
count = 0
i = 0

while i < len(colors):
    count += 1
    i += 1
print(count)

#11. Given a list of numbers, print only the odd numbers using a while loop.

numbers = [1,2,5,6,7,8,9,10,11,12,13,14,15]

num1=0
while num1 < len(numbers):
    if numbers[num1] % 2 != 0:
        print(numbers[num1])
    num1 += 1

#12. Write a program that prints numbers from 1 to 10, but skips 5 using continue.

for number in range(1,11):
    if number == 5:
        continue
    print(number)

#13. Write a program to sum all elements of a list using a while loop.

number_list = [1,2,12,15,40]

sumNum = 0
s=0

while s < len(number_list):
    sumNum += number_list[s]
    s += 1
print(sumNum)

#14. Write a program to find the largest number in a list.

print(max(number_list))

#15. Given a list of names, print all names except "Admin" using continue.

namesList = ['User','Tester','Admin','Anonymous']

for names in namesList:
    if names == 'Admin':
        continue
    print(names)

#16. Write a program to check whether a given number exists in a list.

numList = [1,7,12,25,18,20,19]
num2 = int(input('Enter a number: '))

if num2 in numList:
    print("Number exists in a list")
else:
    print("Number doesn't exist in a list")

#17. Write a program to print all elements at even index positions in a list.

even_index= [1,2,3,4,5,6,7]
n=0
while i < len(even_index):
    print(even_index[n])
    n += 2


