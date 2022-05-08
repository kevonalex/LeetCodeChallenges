# receive integer input, n
# create internal list of values up to and incl. n (1st loop)
# contain list within second list with other variables preceding it (2nd loop)
# return output

import numpy as np


def ListReturn(n):
    L1=[]
    L2=[]
    Output=[0]*n
    if n <=0:
        #print("[]")
        pass
    else:
        for x in range(0,n):
            L2+=[x+1]
            Output[x]=CloneList(L2)
    print(Output)

def CloneList(L1):
    L2 = L1[:]
    return L2

ListReturn(-2)