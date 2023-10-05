n = int(input())

graph = {}
for i in range(n):
    x,y,z = input().split()
    graph[x] = [y,z]

def preorder(root,order):
    order.append(root)
    if not root in graph.keys():
        return order
    left,right = graph[root]
    if left != ".":
        order = preorder(left,order)
    if right != ".":
        order = preorder(right,order)

    return order

def inorder(root,order):
    if not root in graph.keys():
        return order
    left,right = graph[root]
    if left != ".":
        order = inorder(left,order)
    order.append(root)
    if right != ".":
        order = inorder(right,order)
    return order

def postorder(root,order):
    if not root in graph.keys():
        return order
    left,right = graph[root]
    if left != ".":
        order = postorder(left,order)
    if right != ".":
        order = postorder(right,order)
    order.append(root)
    return order

print("".join(preorder("A",[])))
print("".join(inorder("A",[])))
print("".join(postorder("A",[])))