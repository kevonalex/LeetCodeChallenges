#receive integer input
#convert to decimal representation
#search for odd digits
#if condition using bool
import numpy as np
import decimal
from decimal import Decimal

InputInt = 3.00005

def DecRep(InputInt):
    Output = []
    OddDigit=False
    count=0
    IntDecimals = InputInt*(10^5)
    DecimalNumber=int(IntDecimals)
    for a in str(IntDecimals):
        DecCheck=DecimalNumber%2
        if DecCheck != 0:
            OddDigit=True
            break
        else:
            continue
    print(OddDigit)
    return OddDigit

DecRep(InputInt)

#RESULTS
#TC: O(N^2)
#SC: O(4)