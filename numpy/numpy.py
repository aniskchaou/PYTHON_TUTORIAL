import numpy as np

list1=[ 1.73 , 1.68 , 1.71 , 1.89 , 1.79]
list2=[ 65.4 , 59.2 , 63.6 , 88.4 , 68.7]

#transform list to numpy array
numpy_list1=np.array(list1)
print "numpy_list1 : "+str(numpy_list1)

numpy_list2=np.array(list2)
print "numpy_list2 : "+str(numpy_list2)

#addition
numpy_list3=numpy_list1+numpy_list2
print "numpy_list1 + numpy_list2 : "+str(numpy_list3) 



#output
#numpy_list1 : [1.73 1.68 1.71 1.89 1.79]
#numpy_list2 : [65.4 59.2 63.6 88.4 68.7]
#numpy_list1 + numpy_list2 : [67.13 60.88 65.31 90.29 70.49]







import numpy as np

list3=[1.0 , "is", True ]
#NumPy arrays : contain only one type
numpy_array=np.array(list3)
print numpy_array


#concatenation and addition
python_list = [1 , 2, 3]
numpy_list=np.array(python_list)

print "python_list+python_list"
print python_list+python_list

print "numpy_list+numpy_list"
print numpy_list+numpy_list

print "numpy_list+python_list"
print numpy_list+python_list

#output
#['1.0' 'is' 'True']
#python_list+python_list
#[1, 2, 3, 1, 2, 3]
#numpy_list+numpy_list
#[2 4 6]
#numpy_list+python_list
#[2 4 6]




import numpy as np

list1=[ 1.73 , 1.68 , 1.71 , 1.89 , 1.79]
list2=[ 65.4 , 59.2 , 63.6 , 88.4 , 68.7]

#transform list to numpy array
numpy_list1=np.array(list1)

print "numpy_list1[1] : "
print numpy_list1[1]

print "numpy_list1>1.80 : "
print numpy_list1>1.80

print "numpy_list1[numpy_list1>1.80] : "
print numpy_list1[numpy_list1>1.80]


#output
#numpy_list1[1] : 
#1.68
#numpy_list1>1.80 : 
#[False False False  True False]
#numpy_list1[numpy_list1>1.80] : 
#[1.89]






import numpy as np

list_2d=[[ 1.73 , 1.68 , 1.71 , 1.89 , 1.79],
[ 65.4 , 59.2 , 63.6 , 88.4 , 68.7]]

#2d numpy array
numpy_array2d=np.array(list_2d)

print "numpy_array2d : "
print numpy_array2d

print "numpy_array2d shape : "
print numpy_array2d.shape


#output
#numpy_array2d : 
#[[ 1.73  1.68  1.71  1.89  1.79][65.4  59.2  63.6  88.4  68.7 ]]
#numpy_array2d shape : 
#(2, 5)






import numpy as np

list_2d=[[ 1.73 , 1.68 , 1.71 , 1.89 , 1.79],
[ 65.4 , 59.2 , 63.6 , 88.4 , 68.7]]

#2d numpy array
numpy_array2d=np.array(list_2d)

print "numpy_array2d[0] : "
print numpy_array2d[0]

print "numpy_array2d[0][2] : "
print numpy_array2d[0][2]

print "numpy_array2d[:,1:3] : "
print numpy_array2d[:,1:3]

print "numpy_array2d[1,:] : "
print numpy_array2d[1,:]









import numpy as np


height = np . round ( np . random . normal (1.75 , 0.20 , 5000) , 2)

weight = np . round ( np . random . normal (60.32 , 15 , 5000) , 2)

np_city = np . column_stack (( height , weight ) )

print np_city
print np.mean ( np_city [: ,0])
print np.median ( np_city [: ,0])
print np.corrcoef ( np_city [: ,0] , np_city [: ,1])
print np.std ( np_city [: ,0])