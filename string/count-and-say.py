class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        def rle(_str):
            if not _str:
                return ""
                
            N = len(_str)
            res = ""
            l = 0

            for r in range(N):
                counts = r - l + 1
                
                if _str[l] != _str[r]:
                    res += str(counts - 1) + str(_str[l])
                    l = r

            res += str(N - l) + str(_str[l])

            return res

        if n == 1:
            return "1"
        return rle(self.countAndSay(n - 1))
        

                
