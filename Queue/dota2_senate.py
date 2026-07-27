class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r = deque()
        d = deque()

        n = len(senate)
        for i in range(n):
            if senate[i] == "R":
                r.append(i)
            else:
                d.append(i)
        while r and d:
            r_senate = r.popleft()
            d_senate = d.popleft()

            if d_senate < r_senate:
                d.append(d_senate + n)
            else:
                r.append(r_senate + n)

        
        return "Radiant" if r else "Dire"