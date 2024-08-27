class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True
    
        
        second = 0
        for x in range(len(t)):
            if t[x] == s[second]:
                second+=1
            if second == len(s):
                return True
        return False


solution = Solution()
s = "abc"
t = "ahbgdc"
print(solution.isSubsequence(s,t))
