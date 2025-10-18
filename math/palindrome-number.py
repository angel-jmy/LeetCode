class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # x = str(x)
        # N = len(x)
        # mid = N // 2

        # for i in range(mid):
        #     if x[i] != x[N - i - 1]:
        #         return False

        # return True

        if x < 0:
            return False

        orig = x
        pal = 0

        while x > 0:
            pal = 10 * pal + x % 10
            x //= 10

        if orig == pal:
            return True

        return False