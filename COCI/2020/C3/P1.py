class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False  

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.end = True

    def can_move(self, word):
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                return False
        return True


n = int(input())  
nina_trie = Trie()
for _ in range(n):
    nina_trie.insert(input().strip())
m = int(input())  
emilija_trie = Trie()
for _ in range(m):
    emilija_trie.insert(input().strip())
memo = {}
def can_win(is_nina_turn, current_word):
    if (is_nina_turn, current_word) in memo:
        return memo[(is_nina_turn, current_word)]
    if is_nina_turn:
        trie = nina_trie
    else:
        trie = emilija_trie
    for char in 'abcdefghijklmnopqrstuvwxyz':
        new_word = current_word + char
        if trie.can_move(new_word):
            if not can_win(not is_nina_turn, new_word):
                memo[(is_nina_turn, current_word)] = True
                return True
    memo[(is_nina_turn, current_word)] = False
    return False
if can_win(True, ""):
    print("Nina")
else:
    print("Emilija")