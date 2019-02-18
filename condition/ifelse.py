#Python Conditions and If statements
#Python supports the usual logical conditions from mathematics:

#Equals: a == b
#Not Equals: a != b
#Less than: a < b
#Less than or equal to: a <= b
#Greater than: a > b
#Greater than or equal to: a >= b
#These conditions can be used in several ways, most commonly in "if statements" and loops.

a = 33
b = 200
if b > a:
  print("b is greater than a")
  


#Indentation
#Python relies on indentation, using whitespace, to define scope in the code.
#Other programming languages often use curly-brackets for this purpose.

#If statement, without indentation (will raise an error):

#a = 33
#b = 200
#if b > a:
#print("b is greater than a") # you will get an error
  
 
    
#Elif
#The elif keyword is pythons way of saying "if the previous conditions were not true, 
#then try this condition".

a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal") 
#In this example a is equal to b, so the first condition is not true, but the elif condition 
#is true, so we print to screen that "a and b are equal".



#Else
#The else keyword catches anything which isn't caught by the preceding conditions.


a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

#You can also have an else without the elif:

a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")



#Short Hand If
#If you have only one statement to execute, you can put it on the same line as the if statement.
if a > b: print("a is greater than b")


#Short Hand If ... Else
#If you have only one statement to execute, one for if, and one for else, you can put it
# all on the same line:


print("A") if a > b else print("B")
#You can also have multiple else statements on the same line:

print("A") if a > b else print("=") if a == b else print("B")



#And
#The and keyword is a logical operator, and is used to combine conditional statements:
#Test if a is greater than b, AND if c is greater than a:

if a > b and c > a:
  print("Both conditions are True")


#Or
#The or keyword is a logical operator, and is used to combine conditional statements:
#Test if a is greater than b, OR if a is greater than c:

if a > b or a > c:
  print("At least one of the conditions is True")