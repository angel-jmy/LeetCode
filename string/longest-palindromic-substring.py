class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def expandAroundCenter(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]  # return valid palindrome

        longest = ""
        for i in range(len(s)):
            # Odd-length palindrome
            odd = expandAroundCenter(i, i)
            # Even-length palindrome
            even = expandAroundCenter(i, i + 1)
            # Take the longer one
            longest = max(longest, odd, even, key=len)

        return longest