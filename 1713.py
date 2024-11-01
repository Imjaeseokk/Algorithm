import heapq

N = int(input())
R = int(input())

recommendations = list(map(int,input().split()))

photo = {}


# print(min(dictionary, key = lambda x:x[1]))

for i, student in enumerate(recommendations):
    if student in photo:
        photo[student][0] += 1
    else:
        if len(photo) == N:     # N칸 꽉 참
            sorted_photo = sorted(photo.items(), key = lambda x:(x[1][0],x[1][1]))
            remove_photo = sorted_photo[0][0]
            del photo[remove_photo]
            photo[student] = [1,i]
        else:                   # 안 참
            photo[student] = [1,i]

print(*sorted(photo.keys()))
