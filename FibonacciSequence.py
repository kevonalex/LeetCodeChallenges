import numpy as np
#1. Fibonacci Sequence

# define function with int input of 100
# input fibonacci sequence function into equation
# find even numbers in algorithm as part of process and add to summation variable
# implement loop to continue adding until first 100 numbers are reached
# return sum of numbers within this variable
# evaluate time and space complexity

f=np.array([0,0])
f[0]=1
f[1]=1
even_nums=[0]
a=0
while len(even_nums)<10:
    a += 1
    f=np.append(f,f[a]+f[a-1])
    fsum=f[a]+f[a-1]
    #print(fsum)
    if fsum%2 == 0:
        even_nums=np.append(even_nums,[f[a]+f[a-1]])
    else:
        continue
output=sum(even_nums)
print(output)

#PROGRAM RESULTS
#TC: O(n^2) , low efficiency, improve by avoiding nested loop
#SC: O(4), 4 variables used, improve by combining steps 3 and 4 in beginning