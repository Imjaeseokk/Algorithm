class Trie(object):
    def __init__(self):
        self.head = {}

    def add(self,things):
        current_node = self.head

        for i in things:
            if i not in current_node:
                current_node[i] = {}
            current_node = current_node[i]
        current_node = i

    def show(self,root,level):
        current_node = root
        if current_node.values() == [{}]:
            return

        for i in sorted(current_node):
            print(" "*level+i)
            if current_node[i]:
                self.show(current_node[i],level+1)

N = int(input())
trie = Trie()

for i in range(N):
    directories = list(input().split("\\"))
    # print(directories)
    trie.add(directories)

trie.show(trie.head,0)