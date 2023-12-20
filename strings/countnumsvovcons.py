str="123abcDEF$$"
nums=0
vov=0
con=0
spc=0
for i in str:
    if (i>='a'and i<='z')or (i>='A' and i<='Z'):
        i=i.lower()
        if i=='a'or i=='e' or i=='i' or i=='o' or i=='u':
            vov+=1
        else:
            con+=1
    elif i.isdigit():
        nums+=1
    else:
        spc+=1
print(f'Number of vowels: {vov} Number of Consonants: {con} Number of digits: {nums} Number of special {spc}')