class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        def expandAroundCenter(left, right):
            count = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            return count

        total = 0
        for i in range(len(s)):
            total += expandAroundCenter(i, i)     # Odd-length palindromes
            total += expandAroundCenter(i, i + 1) # Even-length palindromes

        return total