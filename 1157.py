word = input()
dict = {}
for w in word:
    if ord(w) >= 97:
        c = chr(ord(w)-32)
    else:
        c = w
    if not c in dict.keys():
        dict[c] = 1
    else:
        dict[c] += 1


tolist = (sorted(dict.items(),key = lambda x:x[1],reverse = True))

if len(tolist) > 1:
    if (tolist[0][1] == tolist[1][1]):
        print("?")
    else:
        print(tolist[0][0])
else:
    print(tolist[0][0])