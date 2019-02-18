#Almost everything in Python is an object, with its properties and methods.
#A Class is like an object constructor, or a "blueprint" for creating objects.

#Create a Class
#To create a class, use the keyword class:
#Example
#Create a class named MyClass, with a property named x:

class MyClass:
  x = 5

#Create Object
#Now we can use the class named myClass to create objects:
#Example
#Create an object named p1, and print the value of x:

p1 = MyClass()
print(p1.x)


#The __init__() Function

#All classes have a function called __init__(), which is always executed when the
#class is being initiated.

#Use the __init__() function to assign values to object properties, or other operations
# that are necessary to do when the object is being created:
#Example
#Create a class named Person, use the __init__() function to assign values for name and age:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)
#Note: The __init__() function is called automatically every time the class is being used to create a new object.


#Object Methods
#Objects can also contain methods. Methods in objects are functions that belongs to the object.
#Let us create a method in the Person class:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()

#Note: The self parameter is a reference to the class instance itself, and is used to access
#variables that belongs to the class.

#The self Parameter
#The self parameter is a reference to the class itself, and is used to access variable
#s that belongs to the class.

#It does not have to be named self , you can call it whatever you like, but it has to be the first 
#parameter of any function in the class:


class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()

#Modify Object Properties
#You can modify properties on objects like this:

p1.age = 40

#Delete Object Properties
#You can delete properties on objects by using the del keyword:


del p1.age


#Delete Objects
#You can delete objects by using the del keyword:
#Delete the p1 object:

del p1