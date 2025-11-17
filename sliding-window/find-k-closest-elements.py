class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        N = len(arr)
        mid = bisect_left(arr, x)
        if mid >= N:
            mid = N - 1
        elif mid > 0:
            if arr[mid] - x > x - arr[mid - 1]:
                mid = mid - 1

        
        left_bnd = max(0, mid - k)
        right_bnd = min(N - 1, mid + k)
        # print(mid, left_bnd, right_bnd)

        l = left_bnd
        min_sum = float('inf')
        cur_sum = 0
        res = [-1, -1]
        for r in range(left_bnd, right_bnd + 1):
            cur_sum += abs(arr[r] - x)
            if r - l + 1 == k:
                if cur_sum < min_sum:
                    min_sum = cur_sum
                    res = [l, r]
                cur_sum -= abs(arr[l] - x)
                l += 1

        return arr[res[0]:res[1] + 1]


