from sys import stdin


def reverseEachWord(string):
    li = string.split()
    for i in range(len(li)):
        li[i]=li[i]
    return li


# main
string = stdin.readline().strip()

ans = reverseEachWord(string)

print(ans)