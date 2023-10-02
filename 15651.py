n,m = map(int,input().split())

numbers = [i for i in range(1,n+1)]
answer = []
def backTracking(answer):
    if len(answer) >= m:
        print(*answer)
        return answer
    for i in numbers:
        answer.append(i)
        backTracking(answer)
        answer.pop()

backTracking(answer)
