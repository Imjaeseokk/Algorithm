class Node(object):
    def __init__(self,key,data = None):
        self.key = key
        self.data = data
        self.children = {}

class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self,foods):
        current_node = self.head

        for food in foods:
            if food not in current_node.children:
                current_node.children[food] = Node(food)
            current_node = current_node.children[food]
        current_node.data = food

    def travel(self, level, root):
        # for i in root.children:
        #     print(root.children[i], type(root.children[i]))
        #

        current = root
        if not current.children:
            return

        for food in sorted(current.children):
            print("--" * level,food,sep="")
            self.travel(level+1,current.children[food])


trie = Trie()

N = int(input())
for i in range(N):
    input_list = list(input().split())
    length = int(input_list.pop(0))
    trie.insert(input_list)

trie.travel(0,trie.head)

