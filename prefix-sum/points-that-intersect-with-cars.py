class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        nums.sort()  # sort by start, then end
        start0, end0 = nums[0]
        counter = end0 - start0 + 1
        cur_end = end0

        for a, b in nums[1:]:
            if a > cur_end:
                # disjoint: add whole interval
                counter += b - a + 1
                cur_end = b
            else:
                # overlap: only add what's beyond cur_end
                add = max(0, b - cur_end)
                counter += add
                cur_end = max(cur_end, b)

        return counter
