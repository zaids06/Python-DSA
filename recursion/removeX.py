# Problem: Remove x from string
def removeX(string):
    length =len(string)
    if length==0:
        return string
    smallerString=removeX(string [1:])
    if string[0]=='x':
        return smallerString
    else:
        return string[0]+smallerString

# Main
string = input()
print(removeX(string))
