def stringToInteger(s):
    length=len(s)
    if length==1:
        return int(s)
    mul=10**(length-1)
    return int(s[0])*mul+stringToInteger(s[1:])

string=input()
print(stringToInteger(string))