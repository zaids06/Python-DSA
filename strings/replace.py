def replace(str,char1,char2):
    str2=""
    for chr in str:
        if chr == char1:
            str2+=char2
        else:
            str2+=chr
    return str2
str="aabbcaadd"
final=replace(str,'a','e')
print(final)
