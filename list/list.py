#The list is a most versatile datatype available in Python which can be written as a list of comma-separated values (items) between square brackets. 

#Important thing about a list is that items in a list need not be of the same type.
list1 = ['physics', 'chemistry', 1997, 2000];
list2 = [1, 2, 3, 4, 5 ];
list3 = ["a", "b", "c", "d"]

print "list1[0]: ", list1[0]
print "list2[1:5]: ", list2[1:5]

#updating list
print "Value available at index 2 : "
print list1[2]
list1[2] = 2001;
print "New value available at index 2 : "
print list1[2]

#deleting element
print list1
del list1[2];
print "After deleting value at index 2 : "
print list1





#output
#list1[0]:  physics
#list2[1:5]:  [2, 3, 4, 5]
#Value available at index 2 : 
#1997
#New value available at index 2 : 
#2001
#['physics', 'chemistry', 2001, 2000]
#After deleting value at index 2 : 
#['physics', 'chemistry', 2000]



list1 = ['physics', 'chemistry', 1997, 2000];
list2 = [1, 2, 3, 4, 5 ];
list3 = ["a", "b", "c", "d"]

#Length
print "Length : "+str(len([1, 2, 3]))
#Concatenation
list4=[1, 2, 3] + [4, 5, 6]
print "Concatenation : "+str(list4)
#Repetition
list5=['Hi!'] * 4
print "Repetition : "+str(list5)
#Membership
print "Membership : "+str(3 in [1, 2, 3]) 
#Iteration : 
print "iteration : "
for x in [1, 2, 3]: 
  print x,



#output
#Length : 3
#Concatenation : [1, 2, 3, 4, 5, 6]
#Repetition : ['Hi!', 'Hi!', 'Hi!', 'Hi!']
#Membership : True
#iteration : 
#1 2 3



list1 = ['physics', 'chemistry', 1997, 2000,1997];
list2 = [1, 2, 3, 4, 5 ];
list3 = ["a", "b", "c", "d"]


#Compares elements of both lists.
print "cmp : "+str(cmp(list1, list2))

	
#Returns item from the list with max value.
print "max : "+str(max(list1))
	
#Returns item from the list with min value.
print "min : "+str(min(list1))


	
#Appends object obj to list
print "append : "+str(list1.append("hello"))
	
#Returns count of how many times obj occurs in list
print "count : "+str(list1.count(1997))
	
#add the content to existing list.
print "extend : "+str(list1.extend(list2))

#Returns the lowest index in list that obj appears
print "index : "+str(list1.index(2000))

	
#Inserts object obj into list at offset index
print "insert : "+str(list1.insert(2, "hello !"))

	
#Removes and returns last object or obj from list
print "pop(2) : "+str(list1.pop(2))

#removes the last object from the list
print "pop : "+str(list1.pop())

#Reverses objects of list in place
print "reverse : "+str(list2.reverse())
print list2	
#Sorts objects of list, use compare func if given
print "sort : "+str(list2.sort())
print list2
#Removes object obj from list
print "remove : "+str(list2.remove(1))
print list2


#output
#cmp : 1
#max : physics
#min : 1997
#append : None
#count : 2
#extend : None
#index : 3
#insert : None
#pop(2) : hello !
#pop : 5
#reverse : None
#[5, 4, 3, 2, 1]
#sort : None
#[1, 2, 3, 4, 5]
#remove : None
#[2, 3, 4, 5]




L = ['spam', 'Spam', 'SPAM!']

print  "L[2] :"+L[2]
print "L[-2] :"+L[-2]
print "L[1:] :"+str(L[1:])

#output
#L[2] :SPAM!
#L[-2] :Spam
#L[1:] :['Spam', 'SPAM!']