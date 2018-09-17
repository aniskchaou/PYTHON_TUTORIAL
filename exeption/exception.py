

#An exception is an event, which occurs during the execution of a program that disrupts the normal flow of the program's instructions.
#When a Python script raises an exception, it must either handle the exception immediately otherwise it terminates and quits.
try:
#A single try statement can have multiple except statements.	
   fh = open("testfile", "w")
   fh.write("This is my test file for exception handling!!")
except IOError:
   print "Error: can\'t find file or read data"
else:
#The code in the else-block executes if the code in the try: block does not raise an exception.	
   print "Written content in the file successfully"
   fh.close()

#output
#Written content in the file successfully




#The finally block is a place to put any code that must execute, whether the try-block raised an exception or not.
try:
   fh = open("testfile", "w")
   fh.write("This is my test file for exception handling!!")
finally:
#You cannot use else clause as well along with a finally clause.
   print "Error: can\'t find file or read data"

#output
#Error: can't find file or read data






#An exception can have an argument, which is a value that gives additional information
#This variable receives the value of the exception mostly containing the cause of the exception.
def temp_convert(var):
   try:
      return int(var)
   except ValueError, Argument:
      print "exception : ", Argument

# Call above function here.
temp_convert("xyz");

#output
#exception :  invalid literal for int() with base 10: 'xyz'




#You can raise exceptions in several ways by using the raise statement.
#raise [Exception [, args [, traceback]]]
#argument is a value for the exception argument. The argument is optional;
#traceback, is also optional (and rarely used in practice)
def determine_level( level ):
   if level < 1:
      raise "Invalid level!", level
determine_level(0)    

#output
#Traceback (most recent call last):
#  File "main.py", line 8, in <module>
#    determine_level(0)      
#  File "main.py", line 7, in determine_level
#    raise "Invalid level!", level
#TypeError: exceptions must be old-style classes or derived from BaseException, not str








#Python also allows you to create your own exceptions by deriving classes from the standard built-in exceptions.
#This is useful when you need to display more specific information when an exception is caught.
class Networkerror(RuntimeError):
   def __init__(self, arg):
      self.args = arg
#The variable e is used to create an instance of the class Networkerror.
try:
   raise Networkerror("Bad hostname")
except Networkerror,e:
   print e.args     


#output
#('B', 'a', 'd', ' ', 'h', 'o', 's', 't', 'n', 'a', 'm', 'e')
