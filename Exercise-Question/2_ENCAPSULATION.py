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


