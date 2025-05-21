"""
Problem: Design Add and Search Words Data Structure
Design a data structure that supports adding new words and finding if a string matches any previously added string. The string may contain '.' where '.' can match any letter.
Implement the WordDictionary class:
- WordDictionary() Initializes the object.
- void addWord(word) Adds word to the data structure.
- bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise.

Example 1:
Input: ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
       [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output: [null,null,null,null,false,true,true,true]
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def search(self, word):
        def dfs(j, node):
            for i in range(j, len(word)):
                char = word[i]
                if char == '.':
                    for child in node.children.values():
                        if dfs(i+1, child):
                            return True
                    return False
                else:
                    if char not in node.children:
                        return False
                    node = node.children[char]
            return node.is_end
        return dfs(0, self.root)
