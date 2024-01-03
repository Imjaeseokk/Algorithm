def backTrack(arr):         # back tracking
    if len(arr) >= 6:
        print(*arr)         # list 원소들을 공백으로 구분하여 출력
        return
    for i in numbers:
        if not arr:         # arr가 비었으면 i 추가
            arr.append(i)
            backTrack(arr)
            arr.pop()
        elif arr[-1] < i:   # arr가 비지 않았으면 가장 오른쪽 원소보가 i가 클 때만 추가
            arr.append(i)
            backTrack(arr)
            arr.pop()

while True:
    tc = list(map(int,input().split()))
    if tc == [0]:
        break
    k,numbers = tc[0],tc[1:]    # 입력값을 분리

    backTrack([])
    print()