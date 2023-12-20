from sys import stdin


def highestOccuringChar(str):
    n = len(str)
    l = [0] * (26)
    for i in str:
        l[ord(i) - 97] += 1
    max=0
    for i in range(0,n):
        if l[max]<l[i]:
            max=i
    return chr(max + 97)


# main
string = stdin.readline().strip();
ans = highestOccuringChar(string)

print(ans)