# print("Here we will learned the difference between numpy and basic python .")


# Required the average temperature 

# Temperature=[22.3,24.5,24.4,23.3,24.3,22.3,22.6]
# total=0
# for temp in Temperature:
#     total+=temp
# avg=total/len(Temperature)
# print("The Temperature of the day=",Temperature)
# print("Average=",avg)


import numpy as np
Temperature=[22.3,24.5,24.4,23.3,24.3,22.3,22.6]
averageTem=np.mean(Temperature)
print(averageTem)

#___Feature of the Numpy is
# Speed=Fast than python 52 time
# Array used for mathematics operation
#use in AI/ML/DL


#___Used Stack market price
#___Used in medical 
#___Image processing


#______Difference between list and Numpy
#_____List________|____________Numpy
#___slow speed____|___________Fast
#____Memory_large_|___________Less Memory
#____Calculation__Fast__|___Slow Calculation
#___For small Data|____For_large Data
 
