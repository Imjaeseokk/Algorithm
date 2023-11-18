d = {"0":"zero","1":"one","2":"two",
              "3":"three","4":"four","5":"five",
              "6":"six","7":"seven","8":"eight",
              "9":"nine"}

book = []

m,n = map(int,input().split())

for i in range(m,n+1):
    s = str(i)
    if len(s) > 1:
        word = d[s[0]]+" "+d[s[1]]
    else:
        word = d[s]
    book.append([word,i])
book = [ans for nope,ans in sorted(book)]
for j in range(len(book)):
    print(book[j],end = " ")
    if (j+1) % 10 == 0:
        print()