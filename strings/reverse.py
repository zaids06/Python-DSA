from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)


def getCompressedString(input) :
    str2=""
    i=0
    while i<len(input) :
        count=1
        while i + 1 < len(input) and input[i] == input[i+1]:
            i+=1
            count+=1
        if count>1:
            str2+=input[i]
            str2+=str(count)
        else:
            str2+=input[i]
        i+=1
    return str2

# Main.
string = stdin.readline().strip();
ans = getCompressedString(string)
print(ans)