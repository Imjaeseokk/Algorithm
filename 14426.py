import sys

input = sys.stdin.readline

N, M = map(int,input().split())
word_list = []
search_list = []
answer = 0
class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}


class Trie(object):
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        curr_node = self.head
        for char in string:
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)
            curr_node = curr_node.children[char]
        curr_node.data = string

    def search(self, string):
        curr_node = self.head
        for char in string:
            if char in curr_node.children:
                curr_node = curr_node.children[char]
            else:
                return False

        return True

trie = Trie()

for i in range(N):
    word = input()[:-1]
    trie.insert(word)

for i in range(M):
    search = input()[:-1]
    answer += int(trie.search(search))


print(answer)