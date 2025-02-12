words = ["apple", "banana", "cherry", "date", "fig"]
sor={}
for word in words:
    sor[word]=len(word)
soreted=sorted(sor,key=lambda x:sor[x])
print(soreted)

# words = ["apple", "banana", "cherry", "date", "fig"]
# sorted_words = sorted(words, key=len)
# print(sorted_words)
