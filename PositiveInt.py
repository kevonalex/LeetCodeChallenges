# receive two values
# generate positive integers up to first value
# divide each positive integer by second value
# given input values are 102030 and 3

def Generator(Val1,Val2):
    ValArray=[]
    Output=0
    for x in range (1,Val1+1):
        ValArray.append(x)
        x+=1
        if x%Val2 == 0:
            Output+=x
    print(Output)

Generator(102030,3)