def contains(s, t):
    length1 = len(s)
    length2 = len(t)
    if length2==0 :
        return True
    if length1 == 0 and length2!=0:
        return False
    elif s[0] == t[0]:
        return contains(s[1:], t[1:])
    return contains(s[1:], t)


s = input()
t = input()

ans = contains(s, t)
if ans is True:
    print('true')
else:
    print('false')