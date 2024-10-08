'''Create a base class Person with attributes name and age.
Then, create a derived class Employee that adds an attribute employee_id.
Write a method in Employee to display all the information.  '''

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Employee ID: {self.employee_id}")
emp = Employee(name="John Doe", age=30, employee_id="E12345")
emp.display_info()

#------------------------------------------------------------------------------------------------------------------------
'''Write a Python program to demonstrate single inheritance where a class Vehicle is inherited by a class Car.
Vehicle should have a method start_engine() and Car should have a method play_music().
Show how you can create a Car object and call both methods.  '''

class Vehicle:
    def __init__(self,name):
        self.name=name
    def start_engine(self):
        print("Engine started!")

class Car(Vehicle):
    def play_music(self):
        print("Playing music in the car!")
    def owner(self):
        print(f"{self.name} is the owner of car")

# Create a Car object
my_car = Car("tim")
# Call methods
my_car.start_engine()
my_car.play_music()
my_car.owner()
print(my_car.name)

#----------------------------------------------------------------------------------------------------------------------------------
'''Implement a class hierarchy where a Shape class is the base class with a method area().
Derive two classes Rectangle and Circle from Shape.
Implement the area() method in both derived classes to calculate the area of a rectangle and a circle, respectively.'''

class Shape:
    def area(self):  # derived class can override this method from base class
        pass
        
class Rectangle(Shape):
    def __init__(self,length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return 3.14 * (self.radius ** 2)

rect = Rectangle(length=4, width=5)
print(f"Rectangle area: {rect.area()}")
circle = Circle(radius=3)
print(f"Circle area: {circle.area()}")

#-----------------------------------------------------------------------------------------------------------------------------------
'''Define a class Animal with a method make_sound().
Create two subclasses Dog and Cat, each overriding the make_sound() method to provide their respective sounds.
Instantiate objects of both subclasses and call their make_sound() methods.'''

class Animal:
    def make_sound(self):
        pass  # Placeholder method

class Dog(Animal):
    def make_sound(self):
        return "Woof!"
class Cat(Animal):
    def make_sound(self):
        return "Meow!"

# Instantiate objects
dog_instance = Dog()
cat_instance = Cat()

# Call make_sound() methods
print(dog_instance.make_sound())  
print(cat_instance.make_sound())  

#------------------------------------------------------------------------------------------------------------------------------------
'''Create a base class Book with attributes title and author, and a derived class EBook that adds an attribute file_size.
Write methods in both classes to display their respective details.
Use the super() function to call the base class method from the derived class'''

class book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
    def publication(self):
        print("{} written by {} published on 2020".format(self.title,self.author))
        
class ebook(book):
    def __init__(self,title,author,file_size):
        super().__init__(title,author)
        self.file_size=file_size
    def online(self):
        print(f"{self.title} is available as ebook in {self.file_size} size on kindle")
    

Book = ebook("cant hurt me","David Goggins","5 mb")  # It is always be derived class
print(Book.title)
print(Book.author)
Book.publication()
print(Book.file_size)
Book.online()

#--------------------------------------------------------------------------------------------------------------------------------------
'''Write a program to demonstrate method overriding. 
Create a class Parent with a method show_message().
Derive a class Child that overrides the show_message() method.
Instantiate a Child object and call the show_message() method to see which version is executed.'''


#----------------------------------------------------------------------------------------------------------------------------------------
'''Implement multiple inheritance in a scenario where a class A has a method method_A(), class B has a method method_B(),
and class C inherits from both A and B. Create an object of class C and call both method_A() and method_B().'''



#--------------------------------------------------------------------------------------------------------------------------------------------
'''Create an abstract class Appliance with an abstract method operate(). 
Derive two classes WashingMachine and Refrigerator from Appliance and implement the operate() method in each.
Instantiate objects of both derived classes and call their operate() methods.'''

from abc import ABC, abstractmethod
# Define the abstract class Appliance
class Appliance(ABC):
    @abstractmethod
    def operate(self):
        pass

# Define the WashingMachine class that inherits from Appliance
class WashingMachine(Appliance):
    def operate(self):
        print("The washing machine is operating.")
    def off(self):                                                             
print("The washing machine is off.")

# Define the Refrigerator class that inherits from Appliance
class Refrigerator(Appliance):
    def operate(self):
        print("The refrigerator is operating.")

# Instantiate objects of the derived classes
washing_machine = WashingMachine()
refrigerator = Refrigerator()

# Call the operate method on each object
washing_machine.operate()
refrigerator.operate()
washing_machine.off()

'''abstract method helps the base class to manipulate their child class  
abstract method is like a restriction imposed on child class   
abstraction method ensures that child class must implement the method of base class
which is a abstract method'''

'''child class may use the base class method or don't use the 
base class metohd with no abstraction'''

'''but the child class must implement the abstract method of base class
otherwisw it will throw the error'''

#---------------------------------------------------------------------------------------------------------------------------------------------
'''Write a Python program where a class Base has a private attribute __secret and a method reveal_secret().
Create a derived class Derived and try to access the private attribute __secret from an object of the derived class. Explain the result.'''

#----------------------------------------------------------------------------------------------------------------------------------------------
'''Design a class hierarchy where Vehicle is the base class with attributes make and model. 
Create a derived class Car that adds an attribute number_of_doors.
Further derive a class ElectricCar from Car that adds an attribute battery_capacity. 
Write methods in each class to display their details and demonstrate the usage.'''

#-----------------------------------------------------------------------------------------------------------------------------------------------
