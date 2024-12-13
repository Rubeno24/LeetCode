class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        y = ''
        for x in s:
            stack.append(x)
            if x == '*':
                stack.pop()
                stack.pop()
        for x in stack:
            y+=x
        return y


x = Solution()
s = "leet**cod*e"
print(x.removeStars(s))