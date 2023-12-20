# Problem ID 91, removeConsecutiveDuplicates
def removeConsecutiveDuplicates(string):
    length =len(string)
    if length==1 or length==0:
        return string
    if string[0]==string[1]:
        short=removeConsecutiveDuplicates(string[2:])
        return string[0]+short
    else:
        short=removeConsecutiveDuplicates(string[1:])
        return string [0]+short

# Main
string = input().strip()
print(removeConsecutiveDuplicates(string))
