N = int(input())

chemicals = sorted(list(map(int,input().split())))

left = best_left = 0
right = best_right = N-1
feature = new_feature = chemicals[left] + chemicals[right]

while left < right:
    if new_feature < 0:
        left = left + 1
    elif new_feature > 0:
        right = right - 1
    else:
        break

    if left == right:
        break

    new_feature = chemicals[left] + chemicals[right]
    if abs(new_feature) < abs(feature):
        best_left = left
        best_right = right
        feature = new_feature

print(chemicals[best_left],chemicals[best_right])

