n,m = map(int,input().split())

numbers = sorted(list(map(int,input().split())))


def backT(array):
    if len(array) >= m:
        print(*array)
        return None
    for i in numbers:
        if array and array[-1] < i:
            array.append(i)
            backT(array)
            array.pop()
        elif not array:
            if not i in array:
                array.append(i)
                backT(array)
                array.pop()


backT([])