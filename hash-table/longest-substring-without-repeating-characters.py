class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # last_seen = {}
        # N = len(s)

        # if N <= 1:
        #     return N
        
        # last_seen[s[0]] = 0
        # l = 0
        # max_len = 1

        # for r in range(1, N):
        #     if s[r] in last_seen and last_seen[s[r]] != r:
        #         l = max(l, last_seen[s[r]] + 1)
            
        #     last_seen[s[r]] = r
        #     max_len = max(max_len, r - l + 1)

        # return max_len

        N = len(s)
        window = set()

        l = 0

        max_len = 0

        for r in range(N):
            while s[r] in window:
                window.remove(s[l])
                l += 1

            window.add(s[r])

            max_len = max(max_len, r - l + 1)

        return max_len