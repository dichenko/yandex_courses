s = list(input().split())
#print(s)

for i in range(len(s)):
    s[i] = s[i].lower()

#print(s)
dict = {}
for word in s:
    if word in dict:
        dict[word] += 1
    else:
        dict[word]  = 1

for (key) in dict:
    print(key, dict[key])


