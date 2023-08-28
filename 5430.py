import sys

tc = int(input())

for t in range(tc):
    fn = sys.stdin.readline()
    fn = fn.replace("RR", "")
    fn = list(fn)
    n = int(sys.stdin.readline())
    num = str(input())
    num = list(num[1:-1].split(","))
    if n > 0:
        num = list(map(int, num))
    elif n == 0:
        num = []
    r_cnt = 0
    r_flag = False
    r_total = 0
    for f in fn:
        if f == "R":
            r_flag = not r_flag
            r_total += 1
        if f == "D":
            if len(num) <= 0:
                num = 'error'
                break
            if not r_flag:
                num.pop(0)
            else:
                num.pop()


    if type(num) is list:
        if r_flag:
            num.reverse()
        print("[", ",".join(map(str, num)), "]", sep="")
    else:
        print(num)