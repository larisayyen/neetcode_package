
'''
a tree-like structure where each node
represents a single character of a given string.
unlike binary trees, a node may have more than two children.
b - a - d
|
i
|
d
'''

class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.end = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:

        p = self.root

        for char in word:
            index = ord(char) - ord('a')
            if p.children[index] == None:
                p.children[index] = TrieNode()
            p = p.children[index]
        p.end = True

    def search(self, word: str) -> bool:

        p = self.root
        for char in word:
            index = ord(char) - ord('a')
            if p.children[index] == None:
                return False
            p = p.childer[index]
        return p.end

    def startsWith(self, prefix: str) -> bool:

        p = self.root
        for char in prefix:
            index = ord(char) - ord('a')
            if p.children[index] == None:
                return False
            p = p.childer[index]
        return True

############################------#################################
'''
Design a data structure that supports adding new words
and finding if a string matches any previously added string.
'''

class TrieNode:

    def __init__(self):
        self.children = {} # a : TrieNode
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:

        p = self.root

        for char in word:
            if char not in p.children:
                p.children[char] = TrieNode()
            p = p.children[char]

        p.word = True


    def search(self, word: str) -> bool:

        def dfs(n,root):
            p = root

            for i in range(n,len(word)):
                char = word[i]

                if char == '.':
                    for child in p.children.values():
                        if dfs(i+1,child):
                            return True
                    return False

                else:
                    if char not in p.children:
                        return False
                    p = p.children[char]

            return p.word

        return dfs(0,self.root)
