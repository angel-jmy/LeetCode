class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        lstS, lstT = [], []
        for c in s:
            if c != '#':
                lstS.append(c)
            else:
                lstS.pop()

        for c in t:
            if c != '#':
                lstT.append(c)
            else:
                lstT.pop()

        return lstS == lstT