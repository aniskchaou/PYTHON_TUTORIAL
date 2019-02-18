#Creating Variables
#A variable is created the moment you first assign a value to it.

x = 5
y = "John"
print(x)
print(y)

#Variables do not need to be declared with any particular type and can even change type
#after they have been set.

x = 4 # x is of type int
x = "Sally" # x is now of type str
print(x)

#Output Variables
#The Python print statement is often used to output variables.
#To combine both text and a variable, Python uses the + character:

x = "awesome"
print("Python is " + x)

#You can also use the + character to add a variable to another variable:

x = "Python is "
y = "awesome"
z =  x + y
print(z)

x = 5
y = 10
print(x + y)

#If you try to combine a string and a number, Python will give you an error:
#x = 5
#y = "John"
#print(x + y)

