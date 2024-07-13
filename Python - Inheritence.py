# SINGLE-LEVEL INHERITENCE

class Animal:  #parent class
  Name=" "     #parent class instance
  def eat():
    print ("i can eat")  #parent class method
    
class dog(Animal): #child class
  def display(self):
    print("my name is:", self.Name) #child class method

labrador = dog()            # Object Creation of subclass
labrador.Name = "max"
labrador.eat()              # Call the superclass method
labrador.display()          # Call the subclass method

#description:
'''In the single inheritence a child class derives all the  properties from one parent class and the object containes all properties of child class and parent class both
for that reason it is "Single Inheritence" '''

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<,
# MULTIPLE INHERITENCE

class car:             #parent class 1
  def go(self):
    print("it runs")    #parent class method
    
class flyable:         #parent class 2
  def fly(self):
    print("it fly")     #parent class method
    
class flying_car(car,flyable):   #child class
    def char(self):
      print("it can fly and runs both")  #child class method

my_car = flying_car()    # Object Creation of subclass
my_car.go()              # Call the superclass method of parent 1
my_car.fly()             # Call the superclass method of parent 2
my_car.char()            # Call the subclass method

#description:
'''In the multiple  inheritence a child class derives all the  properties from more than one parent class and the object containes all properties of child class and parent classes both
for that reason it is "Multiple Inheritence" '''
