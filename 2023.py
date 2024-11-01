import sys
sys.setrecursionlimit(10**7)

N = int(input())

p = ["2","3","5","7"]

def check_prime(number):
    for i in range(2,int(number**(1/2)+1)):
        if number % i == 0:
            return False
    return True


def backtrack(string):
    if len(string) == N:
        if check_prime(int(string)):
            print(string)
        return

    for i in range(1,10):
        string += str(i)
        if check_prime(int(string)):
            backtrack(string)
        string = string[:-1]

for str_p in p:
    backtrack(str_p)

