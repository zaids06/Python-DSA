def power(a,b):
    if b==1:
        return a
    elif b==0:
        return 1
    return a*power(a,b-1)

print(power(2,3))