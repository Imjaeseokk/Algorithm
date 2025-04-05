import sys

S = input()
T = input()

def dfs(t):
    if t == S:
        print(1)
        sys.exit()
    if len(t) == 0:
        return False
    if t[0] == "B":
        dfs(t[1:][::-1])
    if t[-1] == "A":
        dfs(t[:-1])

dfs(T)
print(0)