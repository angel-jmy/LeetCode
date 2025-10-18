class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        counts = Counter(s)
        
        for i, ch in enumerate(s):
            if counts[ch] == 1:
                return i
                            
        return -1