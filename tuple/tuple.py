#A tuple is a sequence of immutable Python objects. Tuples are sequences, just like lists.
#The differences between tuples and lists are, the tuples cannot be changed unlike lists and tuples use parentheses, 
#whereas lists use square brackets.

tup1 = ('physics', 'chemistry', 1997, 2000);
tup2 = (1, 2, 3, 4, 5 ,6,7);
tup3 = "a", "b", "c", "d";

#print tuples
print "tup1[0]: ", tup1[0];
print "tup2[1:5]: ", tup2[1:5];

# So let's create a new tuple as follows
tup3 = tup1 + tup2;
print tup3
#delete tuple 
del tup3

#output
#tup1[0]:  physics
#tup2[1:5]:  (2, 3, 4, 5)
#('physics', 'chemistry', 1997, 2000, 1, 2, 3, 4, 5, 6, 7)






# Following action is not valid for tuples
tup1[0] = 100;

#output 
# tup1[0] = 100;
#TypeError: 'tuple' object does not support item assignment




#The differences between tuples and lists are, the tuples cannot be changed unlike lists and tuples use parentheses, whereas lists use square brackets.

tup1 = ('physics', 'chemistry', 1997, 2000);
tup2 = (1, 2, 3, 4, 5 ,6,7);
tup3 = ('hi !',)

#Length
print "Length : "+str(len(tup1))

#Concatenation
print "Concatenation : "+str(tup1+tup2)

#Repetition
print "Repetition : "+str(tup3*4)

#Membership
print "Membership : "+str((4 in tup3))

#Iteration
print "iteration : "
for x in tup1:
  print x


#output
#Length : 4
#Concatenation : ('physics', 'chemistry', 1997, 2000, 1, 2, 3, 4, 5, 6, 7)
#Repetition : ('hi !', 'hi !', 'hi !', 'hi !')
#Membership : False
#iteration : 
#physics
#chemistry
#1997
#2000



tup1 = ('physics', 'chemistry', 1997, 2000);
tup2 = ('science',);
list = [1, 2, 3, 4, 5 ,6,7];

#Compares elements of both tuples.
print "cmp : "+str(cmp(tup1, tup2))

#Gives the total length of the tuple.
print "len : "+str(len(tup1))
	
#Returns item from the tuple with max value.
print "max : "+str(max(tup1))

#Returns item from the tuple with min value.
print "min : "+str(min(tup1))

#Converts a list into tuple.
print "tuple : "+str(tuple(list))

#output
#cmp : -1
#len : 4
#max : physics
#min : 1997
#tuple : (1, 2, 3, 4, 5, 6, 7)