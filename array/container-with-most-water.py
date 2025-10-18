class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        N = len(height)
        l, r = 0, N - 1

        max_so_far = -float('inf')

        while l < r:
            length = r - l

            if height[l] < height[r]:
                water = length * height[l]
                
                l += 1
            else:
                water = length * height[r]

                r -= 1

            max_so_far = max(max_so_far, water)

        return max_so_far

