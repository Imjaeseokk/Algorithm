l = int(input())

numbers = list(input())
tonumber = [(ord(i)-96) for i in numbers]
total = 0
for r in range(l):
    total += tonumber[r]*(31**r)

print(total % 1234567891)