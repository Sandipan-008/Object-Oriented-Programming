'''Create a class Person with private attributes name and age. Provide public methods to set and get the values of these attributes. 
Demonstrate how encapsulation is achieved by using these methods to access and modify the private attributes.'''

class Person:
    def __init__(self, name: str, age: int):
        self.__name = name  # private attribute
        self.__age = age  # private attribute
    
    # Getter for name
    def get_name(self) -> str:
        return self.__name
    
    # Setter for name
    def set_name(self, name: str) -> None:
        self.__name = name
    
    # Getter for age
    def get_age(self) -> int:
        return self.__age
    
    # Setter for age
    def set_age(self, age: int) -> None:
        if age > 0:  # Ensure age is a positive integer
            self.__age = age
        else:
            raise ValueError("Age must be positive")

# Demonstration of encapsulation
person = Person("Alice", 30)

# Accessing and modifying private attributes via public methods
print("Name:", person.get_name())  # Output: Alice
print("Age:", person.get_age())  # Output: 30

person.set_name("Bob")
person.set_age(25)
#person.set_age(25)

print("Updated Name:", person.get_name())  # Output: Bob
print("Updated Age:", person.get_age())  # Output: 25

#----------------------------------------------------------------------------------------------------------------------------------------------------
'''Write a Python program that defines a class BankAccount with private attributes account_number and balance.
Provide methods deposit(), withdraw(), and get_balance() to interact with these attributes.
Show how encapsulation protects the balance attribute from being accessed directly.'''

class BankAccount:
    def __init__(self, account_number: str, initial_balance: float = 0.0):
        self.__account_number = account_number  # private attribute
        self.__balance = initial_balance  # private attribute
    
    # Method to deposit money
    def deposit(self, amount: float) -> None:
        if amount > 0:
            self.__balance += amount
        else:
            raise ValueError("Deposit amount must be positive")
    
    # Method to withdraw money
    def withdraw(self, amount: float) -> None:
        if amount > 0:
            if amount <= self.__balance:
                self.__balance -= amount
             
            else:
                raise ValueError("Insufficient funds")
        else:
            raise ValueError("Withdrawal amount must be positive")
    
    # Method to get the current balance
    def get_balance(self) -> float:
        return self.__balance
       
    def accountinfo(self) -> float:
        print(f"your account number is: {self.__account_number}\nand has {self.__balance} rupees")

# Demonstration of encapsulation
sbi = BankAccount("12345678", 100.0)
sbi.accountinfo()

# Accessing and modifying balance via public methods
print("Initial Balance:", sbi.get_balance())  
d = int(input("enter amount to deposit: "))
sbi.deposit(d)
print("Balance after deposit:", sbi.get_balance()) 
w = int(input("enter amount to withdraw: "))
sbi.withdraw(w)
print("Balance after withdrawal:", sbi.get_balance())  
new_bal = sbi.get_balance()
print("new balance is: ",new_bal)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------
'''Implement a class Student with private attributes student_id and grades.
Provide methods to set and get the student_id, and methods to add a grade, remove a grade, and calculate the average grade.
Demonstrate how encapsulation is used to manage the grades list.'''

class Student:
    def __init__(self, student_id: str):
        self.__student_id = student_id  # private attribute
        self.__grades = []  # private attribute
    
    # Getter for student_id
    def get_student_id(self) -> str:
        return self.__student_id
    
    # Setter for student_id
    def set_student_id(self, student_id: str) -> None:
        self.__student_id = student_id
    
    # Method to add a grade
    def add_grade(self, grade: float) -> None:
        if 0.0 <= grade <= 100.0:
            self.__grades.append(grade)
        else:
            raise ValueError("Grade must be between 0 and 100")
    
    # Method to remove a grade
    def remove_grade(self, grade: float) -> None:
        if grade in self.__grades:
            self.__grades.remove(grade)
        else:
            raise ValueError("Grade not found in the list")
    
    # Method to calculate the average grade
    def calculate_average(self) -> float:
        if self.__grades:
            return sum(self.__grades) / len(self.__grades)
        else:
            return 0.0

# Demonstration of encapsulation
student = Student("S12345")
# Accessing and modifying student_id via public methods
print("Student ID:", student.get_student_id())  # Output: S12345
student.set_student_id("S54321")
print("Updated Student ID:", student.get_student_id())  # Output: S54321
# Adding grades
student.add_grade(85.0)
student.add_grade(90.0)
student.add_grade(78.0)
# Calculating average grade
print("Average Grade:", student.calculate_average())  # Output: 84.33
# Removing a grade
student.remove_grade(90.0)
# Calculating average grade after removal
print("Average Grade after removal:", student.calculate_average())  # Output: 81.5

#--------------------------------------------------------------------------------------------------------------------------------------------------------------
'''Design a class Car with private attributes make, model, and year. 
Provide public methods to set and get the values of these attributes, and a method display_info() to print out the car’s details.
Show how encapsulation is used to control access to the car's details.'''

class Car:
    def __init__(self, make: str, model: str, year: int):
        self.__make = make  # private attribute
        self.__model = model  # private attribute
        self.__year = year  # private attribute
    
    # Getter for make
    def get_make(self) -> str:
        return self.__make
    # Getter for model
    def get_model(self) -> str:
        return self.__model 
    # Getter for year
    def get_year(self) -> int:
        return self.__year
     
        
    # Setter for model
    def set_model(self, model: str) -> None:
        self.__model = model
    # Setter for make
    def set_make(self, make: str) -> None:
        self.__make = make
    # Setter for year
    def set_year(self, year: int) -> None:
        self.__year = year
        
    
    # Method to display car details
    def display_info(self) -> None:
        print(f"Car Details:\nMake: {self.__make}\nModel: {self.__model}\nYear: {self.__year}")

# Demonstration of encapsulation
car = Car("Toyota", "Corolla", 2020)

# Accessing and modifying car details via public methods
print("Initial Car Details:")
car.display_info()

# Update car details
car.set_make("Honda")
car.set_model("Civic")
car.set_year(2022)

print("\nUpdated Car Details:")
car.display_info()

# Access individual attributes
print("\nAccessing Individual Attributes:")
print("Make:", car.get_make())  # Output: Honda
print("Model:", car.get_model())  # Output: Civic
print("Year:", car.get_year())  # Output: 2022

#---------------------------------------------------------------------------------------------------------------------------------------------------------------
'''Create a class Library with private attributes books (a list of book titles).
Provide methods to add a book, remove a book, search a book, and list all books.
Demonstrate how encapsulation is used to manage the books list.'''

class Library:
    def __init__(self,section):
        self.__section = section        
        self.__books = []            # class_ attributes
    
    #only way to access private attributes 
    def get_section(self):
        return self.__section
        
    def add_book(self,book):
        self.__books.append(book)

    def remove_book(self,book):
        if book in self.__books:
           self.__books.remove(book)
        else:
            raise ValueError("book not removed")
            
    def search_book(self,book):
        self.__book = book        # method_attribute
        if book in self.__books:
           print(f"the book {self.__book} is founded")
        else:
            raise ValueError("book not found")

    def list_of_books(self):
        print(f"SNU_library has\n{self.__section} section\nand there has books of {self.__books}")

SNU_library = Library("Computer Science")
SNU_library.add_book("Op.system")
SNU_library.add_book("Networking")
SNU_library.add_book("DBMS")
SNU_library.remove_book("DBMS")

SNU_library.list_of_books()
print("SNU_library section: ",SNU_library.get_section())
SNU_library.search_book("Networking")
