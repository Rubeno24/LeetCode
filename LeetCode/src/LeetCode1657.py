from typing import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        hasmap1 = {}
        hasmap2 = {}

        if len(word1) != len(word2):
            return False

        # Count the frequency of each character in both words
        count1 = Counter(word1)
        count2 = Counter(word2)

        # Ensure both words have the same set of unique characters
        if set(count1.keys()) != set(count2.keys()):
            return False

        # Ensure both words have the same frequency distribution
        freq_count1 = Counter(count1.values())
        freq_count2 = Counter(count2.values())

        return freq_count1 == freq_count2
        
        




x = Solution()
word1 = "cabbba"
word2 = "abbccc"
print(x.closeStrings(word1,word2))