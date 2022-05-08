# use merge sort method to return common integers.

#intake both arrays into function
#search both functions for common integers
#save common integers to variable
#save output as set to avoid repetiton
import numpy as np

IntArr1=np.array([1,2,2,2,4,6,8])
IntArr2=np.array([1,2,3,4,5,6,7,8])

def CommonInt(IntArr1, IntArr2):
    if len(IntArr1)>len(IntArr2):
        IntArr1=IntArr2
    output=set()
    for x in IntArr1:
        if x in IntArr2:
            output.add(x)
    print(output)
    return output

CommonInt(IntArr1,IntArr2)

#RESULTS
#TC: O(n^2) due to nested loop
#SC: O(3), 3 variables used