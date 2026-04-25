class TrieNode:
    def __init__(self):
        self.children = {}  #can have up to 26 children nodes(a-z)
        self.endofWord = False 


class PrefixTree:

    def __init__(self):
        self.head = TrieNode()
        

    def insert(self, word: str) -> None:
        self.cur = self.head 
        for idx in range(len(word)):
            letter = word[idx]
            if letter not in self.cur.children:
                self.cur.children[letter] = TrieNode() 
                print(self.cur.children)
            self.cur = self.cur.children[letter]
            if idx==len(word)-1:
                self.cur.endofWord=True


    def search(self, word: str) -> bool:
        self.cur = self.head 
        for idx in range(len(word)): 
            letter = word[idx]
            if letter not in self.cur.children:
                return False
            self.cur = self.cur.children[letter]
        if self.cur.endofWord:
            return True
        return False
        
    def startsWith(self, prefix: str) -> bool:
        self.cur = self.head 
        for letter in prefix: 
            if letter not in self.cur.children:
                return False
            self.cur = self.cur.children[letter]
        return True
        

        
        