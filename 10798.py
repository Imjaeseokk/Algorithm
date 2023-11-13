words = ["" for _ in range(5)]
large = 0

for i in range(5):
    words[i] = input()
    if len(words[i]) > large:
        large = len(words[i])

for j in range(large):
    for w in words:
        if j < len(w):
            print(w[j],end="")

