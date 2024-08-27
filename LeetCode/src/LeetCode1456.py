class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a','e','i','o','u'}
        left=0
        count=0
        result = 0
        for x in range(len(s)):
            count +=1 if s[x] in vowels else 0
            if x - left + 1 > k:
                count -=1 if s[left] in vowels else 0
                left+=1
            result = max(result,count)
        return result


solution = Solution()
s = "abciiidef"
k = 3
print(solution.maxVowels(s,k))