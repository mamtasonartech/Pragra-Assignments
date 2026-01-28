#11. Create a class Student with attributes name and marks, and a method display() to print them.

class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"My name is {self.name}")
        print(f"My marks are {self.marks}")

stu1 = Student("Mamta", 80)
stu1.display()

#12.Write a class Rectangle with attributes length and breadth and a method area() that returns the area.

class Rectangle:
    def __init__(self,length = None, breadth = None):

        if length is None or breadth is None:
            print("Invalid Input")
        if not isinstance(length, (int, float)) or not isinstance(breadth, (int, float)):
            print("Length and breadth must be numbers")
        if length <= 0 or breadth <= 0:
            print("Length and breadth must be greater than 0")
        else:
            self.length = length
            self.breadth = breadth

    def area(self):
        area_of_rectangle = self.length * self.breadth
        print(f"The area of rectangle is : {area_of_rectangle}")

rectangle1 = Rectangle(5,10)
rectangle1.area()
# rectangle2 = Rectangle()
# rectangle2.area()

#13. Define a class BankAccount with attribute balance and methods deposit(amount) and display_balance().

class BankAccount:

    def __init__(self, balance):
        self.balance = balance
    def deposit(self,amount):
        if amount <= 0:
            print("Must be greater than zero")
        else:
            self.balance += amount
    def display_balance(self):
        print(f"The balance is : {self.balance}")

account = BankAccount(1000)
account.deposit(-500)
account.display_balance()

#Write a class Temperature with attribute celsius and a method to_fahrenheit().

class Temperature:
    def __init__(self,celsius = None):
        if celsius is None:
            print("Temperature value is required")

        if not isinstance(celsius, (int, float)):
            print("Temperature must be a number")
        else:
            self.celsius = celsius

    def to_fahrenheit(self):
        fahrenheit = (self.celsius * 9 / 5) + 32
        print(f"Temperature in Fahrenheit is : {fahrenheit}")
temp1 = Temperature(180)
temp1.to_fahrenheit()
# temp1 = Temperature()
# temp1.to_fahrenheit()

#16. Define a class Movie with attributes title and rating and a method is_hit() (rating ≥ 8).

class Movie:
    def __init__(self, title, rating):
        if not isinstance(title, str) or not isinstance(rating, (int, float)):
            raise TypeError("Title must be string and rating must be a number")
        if not isinstance(title, str) or not isinstance(rating, (int, float)):
            raise TypeError("Title must be string and rating must be a number")
        else:
            self.title = title
            self.rating = rating
    def is_hit(self):
        if self.rating >= 8:
            print(f"{self.title} movie is hit")
        else:
            print(f"{self.title} is average")

movie1 = Movie("Moana",8)
movie1.is_hit()
# movie2 = Movie(4, 5)
# movie2.is_hit()

#17. Create a class Counter with attribute count and methods increment() and show().

class Counter:
    def __init__(self,count = 0):
        if not isinstance(count, int):
            print("Count must be an integer")
        elif count < 0:
            print("Count cannot be negative")
        else:
            self.count = count
    def increment(self):
        self.count += 1
    def show(self):
        print(f"The count is : {self.count} ")

counter1 = Counter(2)
counter1.increment()
counter1.show()
# counter1 = Counter("two")
# counter1.increment()
# counter1.show()

#18. Write a class User with attributes username and password, and a method check_password().

class User:
    def __init__(self,username,password):
        if not isinstance(username, str) or not isinstance(password, str):
           print("Username and password must be strings")
        elif not username or not password:
            print("Username and password cannot be empty")
        else:
            self.username = username
            self.password = password
    def check_password(self):
        if self.username == "Admin" and self.password == "Admin" :
            print("Welcome. You entered successfully")
        else:
            print("Incorrect password , try again")

user1 = User("Admin","Admin")
user1.check_password()
user2 = User("User","User")
user2.check_password()
# user3 = User(0,1)
# user3.check_password()

#19. Define a class ShoppingCart with attribute items (list) and method add_item(item).

class ShoppingCart:
    def __init__(self):
        self.items = []
    def add_item(self, item = None):
        if item is None:
            print("Item cannot be None")
            return
        elif not isinstance(item, str):
            print("Item must be a string")
            return
        elif item.strip() == "":
            print("Item cannot be empty")
            return
        else:
            self.items.append(item)

item1 = ShoppingCart()
item1.add_item("Milk")
item1.add_item("Bread")
item1.add_item()
item1.add_item(1)
item1.add_item("Rice")
item1.add_item("Flour")
print(item1.items)

#20. Create a class Vehicle with attributes type and speed, and a method describe().

class Vehicle:
    def __init__(self,type,speed):
        if type is None or speed is None:
            print("Type and speed cannot be None")
        elif not isinstance(type, str) or not type.strip():
            print("Type must be a non-empty string")
        elif not isinstance(speed, (int, float)):
            print("Speed must be a number")
        elif speed < 0:
            print("Speed cannot be negative")
        else:
            self.type = type
            self.speed = speed
    def describe(self):
        print(f"The {self.type} speeds at {self.speed}")

vehicle1 = Vehicle("Audi",40)
vehicle1.describe()
# vehicle2 = Vehicle(0,40)
# vehicle2.describe()

