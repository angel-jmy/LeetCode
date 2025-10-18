class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        ns, np = len(s), len(p)
        countP = Counter(p)
        countS = Counter(s[:np])

        if countP == countS:
            res = [0]
        else:
            res = []

        for end in range(np, ns):
            countS[s[end - np]] -= 1
            countS[s[end]] = countS.get(s[end], 0) + 1
            if countS[s[end - np]] == 0:
                del countS[s[end - np]]

            if countS == countP:
                res.append(end - np + 1)

        return res
            
            
            


