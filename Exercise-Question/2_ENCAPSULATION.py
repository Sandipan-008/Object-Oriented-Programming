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

#-------------------------------------------------------------------------------------------------------------------------------------------------------------
'''Write a Python program that defines a class Rectangle with private attributes length and width.
Provide methods to set and get these attributes, and methods to calculate the area and perimeter of the rectangle.
Show how encapsulation ensures that the rectangle’s dimensions can only be modified through the provided methods.'''

class Rectangle:
    def __init__(self,length,width):
        self.__length = length
        self.__width = width
        
    def cal_area(self):
        self.area = (self.__length*self.__width)
        return self.area
    
    def set_length(self,length):
        self.__length = length
    
    def set_width(self,width):
        self.__width = width
        
    def get_perimeter(self):
        self.perimeter = 2 * (self.__length + self.__width)
        return self.perimeter
        
rectangle = Rectangle(20,15)
rectangle2 = Rectangle(0,0)
print("area of a rectangle is: ",rectangle.cal_area())
rectangle2.set_length(17)
rectangle2.set_width(8)
print("perimeter of a rectangle2 is: ",rectangle2.get_perimeter())

#--------------------------------------------------------------------------------------------------------------------------------------------------
'''Implement a class Employee with private attributes employee_id, name, and salary.
Provide methods to set and get these attributes, and a method apply_raise() to increase the salary by a given percentage.
Demonstrate how encapsulation is used to protect the salary attribute.'''

class Employee:
    def __init__(self,eid,name,salary):
        self.__eid = eid
        self.__name = name
        self.__salary = salary
        
    def set_id(self,eid):
        self.__eid = eid
    def set_name(self,name):
        self.__name = name
    def set_salary(self,salary):
        self.__salary = salary
     
    def  get_all_info(self):
        print(f"\nemployee id : {self.__eid}\nemployee name: {self.__name}\nemployee salary: {self.__salary}\n")
        
      # Method to apply raise to salary
    def apply_raise(self, percentage):
        if percentage >= 0:
           self.__salary += self.__salary * (percentage / 100)
        else:
           raise ValueError("Raise percentage must be non-negative")    
                

employee1 = Employee("","","")
employee1.set_id("e001")
employee1.set_name("Sandipan")
employee1.set_salary(15000)

print("---Employee Details:---")
employee1.get_all_info()
employee1.apply_raise(10)  # 10% raise
print("\n---Employee Details after 10% raise:---")
employee1.get_all_info()

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
'''Design a class PasswordManager with a private attribute password.
Provide methods to set the password, check if a given password is correct, and change the password.
Show how encapsulation is used to manage access to the password.'''

class password_manager:
    
    def __init__(self,name,password):
        self.name = name
        self.__password = password
        
    def set_password(self,password):
        self.__password = password
    def get_password(self):
        return self.__password
        
    def check_password(self,check_p):
        self.check_p = check_p
        if (self.__password == self.check_p):
            print("password check successful")
        else:{
            print("entered a wrong password")
        }
    def reset_password(self,new_p):
        self.__new_password = new_p
        self.__password = self.__new_password
        return self.__password
    def password_desc(self):
        print(f"your password name: {self.name}\nyour password is: {self.__password}")
        
Password = password_manager("facebook"," ")
print("----Enter password to Login----")
lg = input("Enter Password: ")
Password.set_password(lg)
Password.password_desc()
cp = input("enter your facebook password: ")
Password.check_password(cp)

np = input("enter new password: ")
Password.reset_password(np)
Password.password_desc()
print("Your new password : ",Password.get_password())

#-------------------------------------------------------------------------------------------------------------------------------
'''Create a class Order with private attributes order_id, customer_name, and items (a list of item names).
Provide methods to set and get the order ID and customer name, add an item, remove an item, and list all items.
Demonstrate how encapsulation is used to manage the items list.'''

class order:
    def __init__(self,oid,customer,orderlist):
        self.__orderid = oid
        self.__customer_name = customer
        self.__orderList = []
        
    def set_id(self,oid):
        self.__orderid = oid
    def get_id(self):
        return self.__orderid
        
    def set_cname(self,name):
        self.__customer_name = name
    def get_cname(self):
        return self.__customer_name
        
    def add_item(self,item):
        self.__orderList.append(item)
    def remove_item(self,item):
        if item in self.__orderList:
           self.__orderList.remove(item)
        else:{
             print("not in list")
         }
         
    def list_items(self):
        print(self.__orderList)
    
    def order_info(self):
        print(f"Order id [{self.__orderid}] generated by a customer[{self.__customer_name}] who ordered {self.__orderList}\n")
        
          
My_orders = order("","","")
My_orders.set_id("oid001")
My_orders.set_cname("Rajiv")

My_orders.add_item("bread")
My_orders.add_item("butter")
My_orders.add_item("flour")
My_orders.add_item("biscuit")

My_orders.remove_item("biscuit")
My_orders.order_info()

#get the order id
print("ORDER ID: ",My_orders.get_id())

#get the customer name
print("CUSTOMER NAME: ",My_orders.get_cname())

#get the order list
print("---ORDER LIST:---")
My_orders.list_items()

#get the order list after adding item
My_orders.add_item("oil")
print("---ORDER LIST:---")
My_orders.list_items()

#--------------------------------------------------------------------------------------------------------------------------------------------------------------
'''Write a Python program that defines a class Temperature with a private attribute celsius. 
Provide methods to set and get the temperature in Celsius, and methods to convert the temperature to Fahrenheit and Kelvin.
Show how encapsulation is used to control access to the temperature value and its conversions.'''

class temparature:
    def __init__(self,celcius):
        self._celcius = celcius   #protected attribute
        
    def set_temp(self,tem):
        self._celcius = tem
        
    def celcius_to_farenheit(self):
         return (9/5) * self._celcius + 32
    
    def celcius_to_kelvin(self):
        return self._celcius + 273.15
        
        
        
Temparature = temparature("")
t = int(input("enter the temparature: "))  
Temparature.set_temp(t)
print(f"The temparature in celcius  is: {Temparature._celcius} degree celcius")
print(f"The temparature in farenheit is:{Temparature.celcius_to_farenheit()} degree farenheit")
print(f"The temparature in farenheit is: {Temparature.celcius_to_kelvin()} degree kelvin")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------
