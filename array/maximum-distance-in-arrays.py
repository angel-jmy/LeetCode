class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        smallest = arrays[0][0]
        biggest = arrays[0][-1]
        max_distance = 0

        for i in range(1, len(arrays)):
            arr = arrays[i]
            max_distance = max(max_distance, abs(arr[-1] - smallest), abs(biggest - arr[0]))
            smallest = min(smallest, arr[0])
            biggest = max(biggest, arr[-1])

        return max_distance
        
        
        # min1, min2 = float('inf'), float('inf')
        # max1, max2 = -float('inf'), -float('inf')

        # min_idx1, min_idx2 = -1, -1
        # max_idx1, max_idx2 = -1, -1

        # for i in range(len(arrays)):
        #     l = arrays[i]

        #     curr_min, curr_max = l[0], l[-1]
        #     if min1 <= curr_min < min2:
        #         min2 = curr_min
        #         min_idx2 = i

        #     elif curr_min < min1:
        #         min2 = min1
        #         min_idx2 = min_idx1
        #         min1 = curr_min
        #         min_idx1 = i

        #     if max1 >= curr_max > max2:
        #         max2 = curr_max
        #         max_idx2 = i

        #     elif curr_max > max1:
        #         max2 = max1
        #         max_idx2 = max_idx1
        #         max1 = curr_max
        #         max_idx1 = i

        # max_diff = 0
        # for i in range(len(arrays)):
        #     l = arrays[i]
        #     curr_min, curr_max = l[0], l[-1]
        #     if i == max_idx1:
        #         max_diff = max(max_diff, max2 - curr_min)
        #     else:
        #         max_diff = max(max_diff, max1 - curr_min)

        #     if i == min_idx1:
        #         max_diff = max(max_diff, curr_max - min2)
        #     else:
        #         max_diff = max(max_diff, curr_max - min1)

        # return max_diff
