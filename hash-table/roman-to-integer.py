class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        hashmap = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        # subtracts = {'I': ['V', 'X'], 'X': ['L', 'C'], 'C': ['D', 'M']}

        N = len(s)
        if N == 1:
            return hashmap[s[0]]

        num = 0
        i = 0
        while i < N:
            if i < N - 1 and hashmap[s[i]] < hashmap[s[i + 1]]:
                num += hashmap[s[i + 1]] - hashmap[s[i]]
                i += 2
            else:
                num += hashmap[s[i]]
                i += 1

        return num


