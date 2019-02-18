#Time intervals are floating-point numbers in units of seconds. 
#Particular instants in time are expressed in seconds since 12:00am,
#January 1, 1970(epoch).

#There is a popular time module available in Python which provides 
#functions for working with times, and for converting between
#representations. 

#The function time.time() returns the current system time in ticks 
#since 12:00am, January 1, 1970(epoch).


#!/usr/bin/python
import time;  # This is required to include time module.

ticks = time.time()
print "Number of ticks since 12:00am, January 1, 1970:", ticks