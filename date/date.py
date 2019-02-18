#Python Dates
#A date in Python is not a data type of its own, but we can import a module named datetime
#to work with dates as date objects.

import datetime

x = datetime.datetime.now()
print(x)

#Output
#2019-02-16 12:32:47.309081

#Return the year and name of weekday:

import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))


#Creating Date Objects
#To create a date, we can use the datetime() class (constructor) of the datetime module.
#The datetime() class requires three parameters to create a date: year, month, day.

import datetime

x = datetime.datetime(2020, 5, 17)
print(x)


#The strftime() Method
#The datetime object has a method for formatting date objects into readable strings.

import datetime

x = datetime.datetime(2018, 6, 1)
print(x.strftime("%B"))
