class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if (len(s1)+len(s2))!=len(s3):
            return False

        length1 = len(s1)
        length2 = len(s2)
        
        dp = [[0]*(length2+1) for _ in range(length1+1)]
        # row : s2, col: s1
        dp[0][0]= True

        # fill up first col -> entirely made of s1
        for i in range(1,length1+1):
            # if cur idx in s1 matches s3 and prev letters match
            dp[i][0] = s1[i-1]==s3[i-1] and dp[i-1][0]

        # fill up first row -> entirely made of s2
        for j in range(1,length2+1):
            # if cur idx in s2 matches s3 and prev letters match
            dp[0][j] = s2[j-1]==s3[j-1] and dp[0][j-1]     

        for i in range(1,length1+1):
            for j in range(1,length2+1):
                # case 1: new letter is from s1, take prev string from s2 and check if s1 idx match s3 idx
                # case 1: new letter is from s2, take prev string from s1 and check if s2 idx match s3 idx
                dp[i][j] = (dp[i][j-1] and s2[j-1]==s3[i+j-1]) or (dp[i-1][j] and s1[i-1]==s3[i+j-1])
        print(dp) 
        
        return dp[-1][-1]

        