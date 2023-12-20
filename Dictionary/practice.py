s1="hey there this is my dictionary this is something new"
words=s1.split()
dict={}
for word in words:
    dict[word]=dict.get(word,0)+1
print(dict)



