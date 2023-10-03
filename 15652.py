
n,m = map(int,input().split())

numbers = [i for i in range(1,n+1)]

def backTracking(answer):
    if len(answer) >= m:
        print(*answer)
        return answer
    for j in numbers:

        if len(answer) > 0:
            if j >= answer[-1]:
                answer.append(j)
            else:
                continue
        else:
            answer.append(j)
        backTracking(answer)
        answer.pop()

backTracking([])