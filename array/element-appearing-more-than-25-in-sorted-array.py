class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        N = len(arr)
        candidates = [arr[N // 4], arr[N // 2], arr[3 * N // 4]]
        # print(candidates)
        for c in candidates:
            lb = bisect_left(arr, c)
            ub = bisect_right(arr, c) - 1
            if ub - lb + 1 > N // 4:
                return c
