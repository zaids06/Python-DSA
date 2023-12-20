from sys import stdin


def isPermutation(str1, str2):
    n=len(string1)
    m=len(string2)
    l=[0]*(26)
    if n!=m:
        return False
    for i in range(n):
        l[ord(str1[i])-97]+=1
    for i in range(n):
        l[ord(str2[i])-97]-=1
    per=True
    for i in l:
        if i!=0:
            return False
    return True
# Your code goes here


# main
string1 = stdin.readline().strip();
string2 = stdin.readline().strip();

ans = isPermutation(string1, string2)

if ans:
    print('true')
else:
    print('false')

