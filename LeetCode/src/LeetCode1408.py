from collections import deque
from typing import List


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        q = deque(words)
        set1 = set()
        for x in range(len(words)):
            word = q.popleft()
            for j in q:
                if word in j:
                    set1.add(word)
            q.append(word)
        return list(set1)
        

words = ["mass", "as", "hero", "superhero"]

x = Solution().stringMatching(words)
print(x)