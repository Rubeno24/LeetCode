class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        l = 0
        r = len(s)-1
        temp = ''
        s_list = list(s)

        while l<r:
            if s_list[l] not in vowels:
                l+=1
            elif s_list[r] not in vowels:
                r-=1
            else:
                s_list[l], s_list[r] = s_list[r], s_list[l]
                l+=1
                r-=1
        return ''.join(s_list)




solution = Solution()
s = "leetcode"
print(solution.reverseVowels(s))

