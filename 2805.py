n,m = map(int, input().split())
tree = list(map(int, input().split()))
high = max(tree)
low = 1
getTree = 0
while (low <= high):
    height = (high + low)//2

    getTree = 0
    for t in tree:
        if t > height:
            getTree += t-height

    if getTree >= m:
        low = height + 1
    else:
        high = height - 1
    height = (high + low) // 2

print(height)
