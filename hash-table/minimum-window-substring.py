class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # if not s or not t:
        #     return ""

        need = Counter(t)            # characters and counts we need
        window = {}                  # characters in current window
        have = 0                     # how many characters meet required count
        need_size = len(need)        # total unique characters needed

        res = [-1, -1]
        res_len = float("inf")
        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1

            if c in need and window[c] == need[c]:
                have += 1

            # Try to shrink the window from the left
            while have == need_size:
                # Save result if smaller
                if (r - l + 1) < res_len:
                    res = [l, r]
                    res_len = r - l + 1

                # Pop from left
                window[s[l]] -= 1
                if s[l] in need and window[s[l]] < need[s[l]]:
                    have -= 1
                l += 1

        l, r = res
        return s[l:r+1] if res_len != float("inf") else ""