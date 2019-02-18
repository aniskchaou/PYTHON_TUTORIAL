#What is a Module?
#A file containing a set of functions you want to include in your application.

#Create a Module
#To create a module just save the code you want in a file with the file extension .py:

def greeting(name):
  print("Hello, " + name)
  
#Use a Module
#Now we can use the module we just created, by using the import statement:

import mymodule

mymodule.greeting("Jonathan")

#Note: When using a function from a module, use the syntax: module_name.function_name.


