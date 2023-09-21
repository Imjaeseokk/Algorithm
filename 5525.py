n = int(input())
s = int(input())

string = (input())

cnt = 0
cntN = 0
j = 0
while j < s:
    if string[j:j+3] == "IOI":
        cntN +=1
        j+=2
        if n == cntN:
            cnt +=1
            cntN -=1
    else:
        cntN = 0
        j +=1


print(cnt)
