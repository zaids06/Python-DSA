from math import *
from collections import *
from sys import *
from os import *
def check(string):
    length=len(string)
    if length==0:
        return True
    elif length>=3 and string[:3]=="abb":
        return check(string[3:])
    elif length>=2 and string[:2]=="aa":
        return check(string[1:])
    elif length==1 and string[0]=='a':
        return True
    else:
        return False
string=input()
if (check(string)):
    print("true")
else:
    print("false")