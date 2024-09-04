S = list(input())
Q = int(input())

questions = []
for i in range(Q):
    a,l,r = input().split()
    questions.append((a,int(l),int(r)))

summation = [[0 for i in range(len(S)+1)]for i in range(26)]

for i in range(26):
    char = chr(i+97)
    cnt = 0
    for j in range(len(S)):
        if S[j] == char:
            cnt += 1
        summation[i][j+1] = cnt

for c,l,r in questions:
    print(summation[ord(c)-97][r+1]-summation[ord(c)-97][l])