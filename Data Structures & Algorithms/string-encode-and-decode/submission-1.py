class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for word in strs:
            length = len(word)
            string += str(length) + "#"+ word 
        print(string)
        return string
    # 5#Hello5#world
    def decode(self, s: str) -> List[str]:
        output = [] 
        if not s: 
            return [] 

        i = 0 

        while i<len(s):  
            j = i
            # read length until "#" -> for single/multi digit num
            while j<len(s) and s[j]!="#":
                j+=1 
            
            length = int(s[i:j]) 

            # skip delimiter "#" 
            i = j+1 #start index of word 
            word = s[i:i+length]
            output.append(word)
            i +=length
        return output






