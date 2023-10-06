n = int(input())

newNum = ""
cnt = 0
num = n
while newNum != (n):

    if num < 10:
        newNum = int(str(num)*2)
    else:
        newNum = int(str(num%10) + str((num//10 + num%10)%10))
    cnt += 1
    num = int(newNum)
print(cnt)