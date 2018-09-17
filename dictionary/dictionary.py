#Keys are unique within a dictionary while values may not be.
#The values of a dictionary can be of any type
dict={'one':1,'two':2,'thee':3,'four':4,'five':5}
print "dict['one']: ", dict['one']
print "dict['two']: ", dict['two']

#output
#dict['one']:  1
#dict['two']:  2





dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

# update existing entry
dict['Age'] = 8;

# Add new entry 
dict['School'] = "DPS School"; 
print dict

# remove entry with key 'Name'
del dict['Name']; 

# remove all entries in dict
dict.clear(); 

# delete entire dictionary    
del dict ;        

print dict 

#output
#{'School': 'DPS School', 'Age': 8, 'Name': 'Zara', 'Class': 'First'}
#<type 'dict'>





#When duplicate keys encountered during assignment, the last assignment wins.
dict = {'Name': 'Zara', 'Age': 7, 'Name': 'Manni'}
print "dict['Name']: ", dict['Name']

#output
#dict['Name']:  Manni











dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
dict2 = {'Name': 'Zara', 'Age': 7}


#Compares elements of both dict.
print cmp(dict, dict2)


#Gives the total length of the dictionary. This would be equal to the number of items in the dictionary.
print len(dict)

#Produces a printable string representation of a dictionary
print str(dict)

#Returns the type of the passed variable. If passed variable is dictionary, then it would return a dictionary type.
print type(dict)


#output
#1
#3
#{'Age': 7, 'Name': 'Zara', 'Class': 'First'}
#<type 'dict'>





dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}	
dict2 = {'Name': 'Z', }	
#Returns a shallow copy of dictionary dict
dict.copy()

#Create a new dictionary with keys from seq and values set to value.
seq=dict.fromkeys(dict)
print str("New Dictionary : %s " %seq)

#For key key, returns value or default if key not in dictionary
print "Name : "+dict.get('Name')

#Returns true if key in dictionary dict, false otherwise
print "has_key : "+str(dict.has_key('Name'))

#Returns a list of dict's (key, value) tuple pairs
print "items : "+str(dict.items())

#Returns list of dictionary dict's keys
print "keys : "+str(dict.keys())

#Similar to get(), but will set dict[key]=default if key is not already in dict
print "Name : "+dict.setdefault('Name', None)

#Adds dictionary dict2's key-values pairs to dict
dict.update(dict2)
print "dict : "+str(dict)
#Returns list of dictionary dict's values
print "values : "+str(dict.values())

#Removes all elements of dictionary dict
dict.clear()

#output
#New Dictionary : {'Age': None, 'Name': None, 'Class': None} 
#Name : Zara
#has_key : True
#items : [('Age', 7), ('Name', 'Zara'), ('Class', 'First')]
#keys : ['Age', 'Name', 'Class']
#Name : Zara
#dict : {'Age': 7, 'Name': 'Z', 'Class': 'First'}
#values : [7, 'Z', 'First']