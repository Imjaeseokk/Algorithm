N, K = map(int, input().split())

ARR = list(map(int,input().split()))

pt1 = 0
pt2 = 0
max_length = 1
counter = [0 for _ in range(200001)]

counter[ARR[pt1]] = 1

while N > pt2:
    pt1 += 1
    if pt1 == N:
        break

    number_now = ARR[pt1]
    counter[number_now] += 1

    count_now = counter[number_now]

    while count_now > K:
        number_pt2 = ARR[pt2]
        counter[number_pt2] = counter[number_pt2] - 1
        count_now = counter[number_now]
        pt2 += 1

    max_length = max(max_length, pt1 - pt2 + 1)


print(max_length)