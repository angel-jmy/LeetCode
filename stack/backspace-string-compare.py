class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        lstS, lstT = [], []
        for c in s:
            if c != '#':
                lstS.append(c)
            else:
                if lstS:
                    lstS.pop()

        for c in t:
            if c != '#':
                lstT.append(c)
            else:
                if lstT:
                    lstT.pop()

        return lstS == lstT