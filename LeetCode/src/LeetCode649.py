from collections import deque


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        q = deque(senate)
        dBans = 0
        rBans = 0

        while q:
            sentator = q.popleft()
            if sentator == 'R':
                if rBans > 0:
                    rBans -= 1
                else:
                    dBans += 1
                    q.append(sentator)
            elif sentator == 'D':
                if dBans > 0:
                    dBans -= 1
                else:
                    rBans += 1
                    q.append(sentator)
                    
            if all(r == 'R' for r in q):
                return 'Radiant'   
            if all(d == 'D' for d in q):
                return 'Dire'
            



x = Solution()
senate = "RRDDD"
print(x.predictPartyVictory(senate))