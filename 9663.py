N = int(input())

result = []
def check(board,queen):
    for i in range(len(board)):
        if board[i] == queen:
            return False
        elif abs(board[i] - queen) == (len(board)-i):
            return False
    return True



def backTrack(arr):
    if len(arr) >= N:
        result.append(tuple(arr))
        return
    for i in range(1,N+1):
        if check(arr,i):
            arr.append(i)
            backTrack(arr)
            arr.pop()

backTrack([])
print(len(result))