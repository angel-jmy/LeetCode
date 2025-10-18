class Solution(object):
    def countHousePlacements(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        house, space = 1, 1
        total = house + space

        for i in range(1, n):
            house = space
            space = total
            total = (house + space) % MOD

        return total * total % MOD

