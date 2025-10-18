class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1.0
        if n == 1:
            return x
        if n == -1:
            return 1.0 / x

        # handle negatives first (Python ints won't overflow)
        if n < 0:
            return 1.0 / self.myPow(x, -n)

        # exponentiation by squaring
        half = self.myPow(x, n // 2)
        if n % 2 == 0:
            return half * half
        else:
            return half * half * x


        # return self.myPow(x, n - 1) * x
 