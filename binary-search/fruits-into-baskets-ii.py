class Solution(object):
    def numOfUnplacedFruits(self, fruits, baskets):
        """
        :type fruits: List[int]
        :type baskets: List[int]
        :rtype: int
        """
        used = [False] * len(baskets)
        unplaced = 0

        for fruit in fruits:
            placed = False
            for i in range(len(baskets)):
                if not used[i] and baskets[i] >= fruit:
                    used[i] = True  # place fruit in the first (leftmost) available basket
                    placed = True
                    break
            if not placed:
                unplaced += 1

        return unplaced