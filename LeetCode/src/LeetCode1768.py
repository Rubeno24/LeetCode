class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        minLenght = min(len(word1), len(word2))
        newString = ''
        for x in range(minLenght):
            newString += word1[x]
            newString += word2[x]
        newString += word1[minLenght:]+word2[minLenght:]
        return newString


solution = Solution()
word1 = "abcd"
word2 = "pq"
result = solution.mergeAlternately(word1, word2)
print(result)  # Output: "apbqcr"
