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
