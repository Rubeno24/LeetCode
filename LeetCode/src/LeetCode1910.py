class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        racks = []

        for x in s:
            racks.append(x)
            var = ''.join(racks[-len(part):])
            if var == part:
                for x in range(len(part)):
                    racks.pop()
        return ''.join(racks)

 



s = "daabcbaabcbc"
part = "abc"
x = Solution().removeOccurrences(s,part)
print(x)