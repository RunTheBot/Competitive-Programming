class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.node_count = 1  

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
                self.node_count += 1  
            node = node.children[char]
        node.end = True

def count_trie_nodes(words):
    trie = Trie()
    for word in words:
        trie.insert(word)
    return trie.node_count

words = []

try:
    while True:
        word = input().strip()
        if word:
            words.append(word)
except EOFError:
    pass

print(count_trie_nodes(words))
