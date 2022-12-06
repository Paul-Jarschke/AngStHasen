def power(x,n):
    if n==0:
        return 1

    else:
        return(x*power(x,n-1))

def fac(x):
    if x==0:
        return 1
    elif x==1:
        return 1
    else:
        return(x*fac(x-1))

r=1
e=0
i=0
x=int(input("enter x:"))

while r>0.0001:
    r=power(x,i)/fac(i)
    e=e+r
    i=i+1
print(e)