class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = ''.join(ch for ch in s if ch.isalnum())
        s = s.lower()
               
        for i in range(len(s) // 2):
            if s[i] != s[len(s) - i - 1]:
                return False
           
        return True