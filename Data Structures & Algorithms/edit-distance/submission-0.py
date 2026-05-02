class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # DONT NEED TO MODIFY STRING -> just update i/j to simulate the operations
        # i is pointer for word1, j is pointer for word2 

        # memo stores num steps at cur (i,j)
        memo={}
        
        # insert into word1 -> increment j 
        # delete from word1 -> increment i 
        # swap letter in word1 -> increment both i and j 
        # if letter i and j are same -> increment both i and j 
        def recurse(i,j):
            if i>=len(word1):
                # word1 shorter than word2 -> insert (len(word2)-j) num of letters
                return len(word2)-j
            if j>=len(word2):
                # word1 longer than word2 -> delete (len(word1)-i) num of letters
                return len(word1)-i 

            if (i,j) in memo:
                return memo[(i,j)]

            if word1[i]==word2[j]:
                steps = recurse(i+1,j+1)

            else: 
                insert = recurse(i,j+1)
                delete = recurse(i+1,j)
                swap = recurse(i+1,j+1)
                steps = min(insert,delete,swap) +1 
            memo[(i,j)] = steps 
            return steps
        return recurse(0,0)
