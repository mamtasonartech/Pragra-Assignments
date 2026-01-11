#1.Write a while loop to print numbers from 1 to 10.

number = 0
while number < 10:
    number += 1
    print(number)

#2. Write a program to print all even numbers between 1 and 20 using a while loop.

number1 = 1
while  number1<20:
    if number1%2==0:
        print(number1)
    number1 += 1

# 3. Create a list of 5 fruits and print each fruit using a while loop.

fruits = ['apple','banana','orange','strawberry','mango']
if not fruits:
    print("The list is empty")
else:
    num = 0
    while num < len(fruits) :
        print(fruits[num])
        num += 1

# 4. Write a program to print the length of a list.

list_length = len(fruits)
print(list_length)

# 5. Write a program to print all elements of a list using index-based access.

colors = ['red','green','blue','yellow','purple','orange']
if not colors:
    print("The list is empty")
else:
    for col in range(len(colors)):
        print(colors[col])

# 6. Use a while loop to print numbers from 10 to 1.

number3 = 10
while number3 >= 1 :
    print(number3)
    number3 -=1

#7. Write a program that prints numbers from 1 to 5 and stops when the number is 3 using break.

for number4 in range(1,6):
    if number4 ==3 :
        break
    print(number4)

#8. Given a list of integers, print only the first element of the list.

int_list = [1,2,3,4,5]
if not int_list:
    print("The list is empty")
else:
    print(int_list[0])
