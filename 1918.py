formula = list(input())


operator_stack = []
oper = {"*":1,"/":1,"+":0,"-":0,"(":-1, ")":-1}
result = []

for i in formula:
    if ord(i) >= 65 and ord(i) <= 90:
        result.append(i)
    else:
        if i == "(":
            operator_stack.append(i)
        elif i == ")":
            while operator_stack and operator_stack[-1] !="(":
                result.append(operator_stack.pop())
            if operator_stack[-1] =="(":
                operator_stack.pop()
        else:
            while operator_stack and oper[operator_stack[-1]] >= oper[i]:
                result.append(operator_stack.pop())
            operator_stack.append(i)

while operator_stack:
    o = operator_stack.pop()
    if not o == "(" and not o == ")":
        result.append(o)

print("".join(result))