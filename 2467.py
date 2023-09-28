n = int(input())

chemical = list(map(int,input().split()))

solution = 2000000001

left = 0
right = n-1
while left < right:
    feature = chemical[right] + chemical[left]
    if feature == 0:
        result = (chemical[left], chemical[right])
        break

    if abs(feature) < solution:
        solution = abs(feature)
        result = (chemical[left],chemical[right])

    elif feature > 0:
        right -= 1
    elif feature < 0:
        left += 1

print(*result)
