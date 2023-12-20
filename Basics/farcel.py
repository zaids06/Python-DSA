def findGcd(x, y):
    res=min(x,y)
    while(res>=1):
        if((x%res==0) and (y%res==0)):
            return res
        res-=1




t=int(input())
while(t>0):
    x=int(input())
    y=int(input())
    print(findGcd(x,y))