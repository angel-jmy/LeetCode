class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        N = len(arr)
        curr_avg = sum(arr[:k]) / k
        counts = 0
        if curr_avg >= threshold:
            counts += 1
        for i in range(k, N):
            left = i - k
            curr_avg = curr_avg + (arr[i] - arr[left]) / k
            if curr_avg >= threshold:
                counts += 1

        return counts
