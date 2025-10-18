class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        # hashmap = defaultdict(int)
        # left = 0
        # max_len = 0

        # for right in range(len(fruits)):
        #     hashmap[fruits[right]] += 1

        #     while len(hashmap) > 2:
        #         hashmap[fruits[left]] -= 1
        #         if hashmap[fruits[left]] == 0:
        #             del hashmap[fruits[left]]
        #         left += 1

        #     max_len = max(max_len, right - left + 1)

        # return max_len


        hashmap = {}
        left = 0
        max_len = 0

        for right in range(len(fruits)):
            if fruits[right] in hashmap:
                hashmap[fruits[right]] += 1
            elif len(hashmap) <= 1:
                hashmap[fruits[right]] = 1

            else:
                while len(hashmap) >= 2:
                    hashmap[fruits[left]] -= 1
                    if hashmap[fruits[left]] == 0:
                        del hashmap[fruits[left]]
                    left += 1
                hashmap[fruits[right]] = 1

            max_len = max(max_len, right - left + 1)

        return max_len
