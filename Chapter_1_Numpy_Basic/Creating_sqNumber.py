# ______Creating Sequence number 
import numpy as np

# _____Create a sequence of number with specified range ||
#_____/\_____The resulted matrix will 1,3,5,7,9
arr=np.arange(1,10,2)

# print(arr)

#____/\___if you want to print even number upto 100 with jump 5
arr2=np.arange(0,100,5)
# print(arr2)

# The following is the result i have from the terminal
# [ 0  5 10 15 20 25 30 35 40 45 50 55 60 65 70 75 80 85 90 95]

#___we will create an identity matrix
#___with eyes(n) // n is the range

arr3=np.eye(3)
print(arr3)

#___The resulted matrix  i have from the terminal


#[[1. 0. 0.]
 #[0. 1. 0.]
 #[0. 0. 1.]]
