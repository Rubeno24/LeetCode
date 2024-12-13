class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for x in range(len(s)):

            if s[x] != ']' :
                stack.append(s[x])
            else:
                string = ''
                while stack[-1] != '[':
                    string = stack.pop() + string
                stack.pop()
                num = ''
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                stack.append(int(num)*string)
        return "".join(stack)





x = Solution()
s = "3[a]2[bc]"
print(x.decodeString(s))