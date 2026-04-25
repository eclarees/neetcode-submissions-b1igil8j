class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False 

class WordDictionary:

    def __init__(self):
        self.head = TrieNode()
    
    def addWord(self, word: str) -> None:
        self.cur = self.head 
        for idx in range(len(word)):
            letter = word[idx]
            if letter not in self.cur.children:
                self.cur.children[letter] = TrieNode()
                print(self.cur.children)
            self.cur = self.cur.children[letter]
            if idx==len(word)-1:
                self.cur.endOfWord = True

    def search(self, word: str) -> bool:

        def dfs(idx,cur):
            if idx>=len(word):
                return cur.endOfWord #have we completed the word? 
            if word[idx] == ".":
                # try every child:
                for child in cur.children.values(): 
                    if dfs(idx+1,child):
                        return True
                return False
            else: 
                if word[idx] not in cur.children:
                    return False 
                return dfs(idx+1,cur.children[word[idx]])

        return dfs(0,self.head)
        
