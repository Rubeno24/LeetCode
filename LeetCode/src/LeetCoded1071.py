class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1+str2 != str2+str1:
            return ""
        gcdLength = self.gcd(len(str1), len(str2))

        return str1[0:gcdLength]

    def gcd(self, a, b):
        while b != 0:
            remainder = a % b
            a = b
            b = remainder
        return a


solution = Solution()
str1 = "ABCDEF"
str2 = "ABC"
anw = solution.gcdOfStrings(str1, str2)
print(anw)
