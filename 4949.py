sentence = " "

while sentence != ".":
    sentence = input()
    if sentence == ".":
        break
    stack = []
    for word in sentence:
        if word == "(" or word == "[":
            stack.append(word)

        if word == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                word = False
                break

        if word == "]":
            if stack and stack[-1] == "[":
                stack.pop()
            else:
                word = False
                break
    if not stack and word == ".":
        print("yes")
    else:
        print("no")


