class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        N = len(arr2)
        # print(bisect_left(arr2, 5))

        def get_closest_diff(target):
            idx = bisect_left(arr2, target)
            if idx >= N:
                return target - arr2[idx - 1]
            if idx == 0:
                return arr2[idx] - target

            return min(arr2[idx] - target, target - arr2[idx - 1])
            

        counter = 0

        for num in arr1:
            diff = get_closest_diff(num)
            # print(diff)
            if diff > d:
                counter += 1

        return counter
