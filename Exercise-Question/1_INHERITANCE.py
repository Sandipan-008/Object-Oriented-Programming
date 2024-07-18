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
