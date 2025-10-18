class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        N = len(ratings)
        candies = [1] * N

        for i in range(1, N):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
        

        for i in range(N - 1, 0, -1):
            if ratings[i - 1] > ratings[i]:
                if candies[i - 1] <= candies[i]:
                    candies[i - 1] = candies[i] + 1

        return sum(candies)