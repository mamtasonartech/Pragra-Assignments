"""21. Create a class BankAccount with methods:
● deposit(amount)
● withdraw(amount)
● display_balance()
Ensure withdrawal is allowed only if balance is sufficient."""

# Create a class named BankAccount
class BankAccount:
# Initialize the account with a balance attribute (default 0)
    def __init__(self,balance = 0):
        self.balance = balance
# Define a deposit method:

    def deposit(self,amount):
        self.balance += amount

# Define a withdraw method:
    def withdraw(self,amount):
        if  amount <= self.balance:
            print("Balance is sufficient")
            self.balance -= amount
        else:
            print("Insufficient balance")

# Define a display_balance method:
#   - It should print the current balance
    def display_balance(self):
        print(f"Current balance is :{self.balance} ")

withdraw1 = BankAccount(1000)
#withdraw1.deposit(1000)
withdraw1.withdraw(500)
withdraw1.display_balance()

print("-----------------------------------------------------------------------------------------------")

"""22. Write a class Student with methods: 
● add_marks(marks_list)
● calculate_average() 
● is_pass() (average ≥ 40) """

# Create a class named Student
class Student:

# Initialize the student with an empty list to store marks
    def __init__(self):
        self.marks = []

# Define add_marks(marks_list) method:
    def add_marks(self,marks_list):
        if not isinstance(marks_list, list):
            print("Please provide a list of marks")
        elif len(marks_list) == 0:
            print("Marks list is empty")
        elif isinstance(marks_list, list):
            self.marks.extend(marks_list)
        else:
            self.marks.append(marks_list)

# Define calculate_average() method:
    def calculate_average(self):
       if len(self.marks)==0:
           return 0
       else:
           return sum(self.marks) / len(self.marks)

# Define is_pass() method:

    def is_pass(self):
        average = self.calculate_average()
        if  average >= 40:
            print("Pass")
        else:
            print("Fail")

student1 = Student()
student1.add_marks([60, 80])
print(student1.marks)
print(student1.calculate_average())
student1.is_pass()

print("-----------------------------------------------------------------------------------------------")

"""23. Create a class LoginSystem with methods: 
● register(username, password) 
● login(username, password) 
Store credentials inside the object. """

# Create a class LoginSystem
class LoginSystem:

# Initialize the class with a data structure (like a dictionary)
    def __init__(self):
        self.credentials = {}

# Define register(username, password) method
    def register(self, username, password):
        if username == "" or password == "":
            print("Username and password cannot be empty")

        if username in self.credentials:
            print("Username already registered")

        self.credentials[username] = password
        print("Registration successful")

# Define login(username, password) method
    def login(self, username, password):
        if username not in self.credentials:
            print("User not found")

        if self.credentials[username] != password:
            print("Incorrect password")

        print("Login successful")

system = LoginSystem()
system.register("admin", "1234")
system.login("admin", "1234")
system.login("admin", "wrong")
system.register("admin", "newpass")

print("-----------------------------------------------------------------------------------------------")
"""24. Define a class LibraryBook with methods: 
● borrow()
● return_book() 
● status() 
Track availability using an instance variable."""

# Create a class named LibraryBook
class LibraryBook:
    def __init__(self,title):
        self.data = {
            "title": title,
            "available": True
        }

# Define borrow() method
    def borrow(self):
        if self.data["available"]== True:
            self.data["available"] = False
            print("Book borrowed successfully")
        else:
            print("Book is already borrowed")
# Define return_book() method
    def return_book(self):
        if self.data["available"]== False:
            self.data["available"] = True
            print("Book returned successfully")
        else:
            print("Book was not borrowed")
# Define status() method

    def status(self):
        if self.data["available"] == True:
            availability = "Book is Available"
        else:
            availability = "Checked Out"
        print(f"The Status is: {availability}")


book1 = LibraryBook("Python")
book1.status()
book1.borrow()
book1.status()
book1.borrow()
book1.return_book()
book1.status()

print("-----------------------------------------------------------------------------------------------")

"""25. Create a class Order with methods: 
● add_item(price)
● calculate_total() 
● apply_discount(percent)"""

# Create a class named Order
class Order:
    # Initialize the class with a data structure (like a list)
    def __init__(self):
        self.items = []
        self.total = 0

    # Define add_item(price) method
    #   - Check if the price is a valid number
    #   - Ensure the price is greater than 0
    #   - Add the price to the items list
    def add_item(self, price=None):
        if price is None:
            print("Invalid Input")
        elif not isinstance(price, (int, float)):
            print("Price must be a number")
        elif price <= 0:
            print("Price must be greater than 0")
        else:
            self.items.append(price)
            print("Item added")
    #   - Check if there are any items in the order
    #   - Calculate the sum of all item prices
    #   - Return or display the total amount
    def calculate_total(self):
        if len(self.items) == 0:
            print("No items in the order")
            return 0
        else:
            self.total = sum(self.items)
            return self.total

    # Define apply_discount(percent) method
    #   - Check if the discount percent is valid (between 0 and 100)
    #   - Calculate the discount based on the current total
    #   - Reduce the total by the discount amount
    #   - Display or return the discounted total
    def apply_discount(self, percent = None):
        if percent is None:
            print("Invalid Percentage")
        if not isinstance(percent, (int, float)):
            print("Percentage must be a number")
            return None
        elif percent < 0 or percent > 100:
            print("Must be between 0 and 100")
            return None
        else:
            total = self.calculate_total()
            discount_amount = total * (percent / 100)
            self.total = total - discount_amount
            return self.total


order1 = Order()
order1.add_item()
order1.add_item(80)

print("Total:", order1.calculate_total())
print("After discount:", order1.apply_discount())
print("After discount:", order1.apply_discount(20))