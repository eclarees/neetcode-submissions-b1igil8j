class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # keep track of first and last occurence of each letter 
        occurence = {} 
        for i in range(len(s)):
            letter = s[i]
            # update last occurence 
            if letter in occurence: 
                occurence[letter] = (occurence[letter][0],i)
            else:
                occurence[letter] = (i,i)

        first = list(occurence.items())[0][1][0]
        last = list(occurence.items())[0][1][1]
        res = []
        for letter, frequency in list(occurence.items())[1:]:
            if frequency[0] < last: 
                # take max of cur last or new frequency's lasy
                last = max(last,frequency[1])
            else: #reset
                res.append(last-first+1)
                first = frequency[0]
                last = frequency[1]

        res.append(last-first+1)
        return res


        