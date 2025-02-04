from typing import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        y = Counter(magazine)

        for x in ransomNote:
            if y[x] > 0:
                y[x] -= 1
            else:
                return False  # not enough characters available
        
        return True  # successfully used all characters





ransomNote = "aaaabbc"
magazine = "ababcbabc"

x = Solution().canConstruct(ransomNote,magazine)
print(x)