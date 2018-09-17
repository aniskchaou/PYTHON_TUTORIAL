#Assertions in Python

#The easiest way to think of an assertion is to liken it to a raise-if statement (or to be more accurate, a raise-if-not statement).

# An expression is tested, and if the result comes up false, an exception is raised.

#If the expression is false, Python raises an AssertionError exception.

#assert Expression[, Arguments]

def kelvinTofahrenheit(temperature):
     #If the expression is false, Python raises an AssertionError exception.
     assert (temperature >= 0),"Colder than absolute zero!"
     return ((temperature-273)*1.8)+32
print kelvinTofahrenheit(273)
print kelvinTofahrenheit(-5)
#If the assertion fails, Python uses ArgumentExpression as the argument for the AssertionError.


#output
#32.0
#Traceback (most recent call last):
#  File "main.py", line 6, in <module>
#    print kelvinTofahrenheit(-5)
#  File "main.py", line 3, in kelvinTofahrenheit
#    assert (temperature >= 0),"Colder than absolute zero!"
#AssertionError: Colder than absolute zero!

