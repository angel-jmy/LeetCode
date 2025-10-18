class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n1, n2 = len(haystack), len(needle)
        for i in range(n1 - n2 + 1):
            if haystack[i: i + n2] == needle:
                return i

        return -1
