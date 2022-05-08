# receive decimal input x
# compute multiple of x by itself in three seperate instances using power
# sum together resultant product of each instance
# return sum

x = 3

def XXFunction(x):
    y=[0,0,0,0]
    for a in range (0,5):
        if a==0:
            y[a]=x*(10**a)
            y[a]+=y[a-1]
        elif a==1:
               y[a]+=x*(10**(a))
               y[a]+=y[a-1]
        elif a==2:
               y[a] += x * (10 ** (a))
               y[a]+=y[a-1]
        elif a==3:
            y[a]+=x * (10 ** a)
            y[a]+=y[a-1]
        a+=1
    ysum = sum(y)
    print(ysum)

XXFunction(x)

#TC: O(N)
#SC: O(3)