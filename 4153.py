numbers = list(map(int,(input().split())))
numbers = sorted(numbers)
while numbers[0] > 0:
    a = numbers.pop()
    b,c = numbers[:]
    if a**2 == (b**2) + (c**2):
        print("right")
    else:
        print("wrong")
    numbers = list(map(int,(input().split())))
    numbers = sorted(numbers)

