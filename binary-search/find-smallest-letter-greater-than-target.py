class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        N = len(letters)
        l, r = 0, N - 1
        while l <= r:
            mid = l + (r - l) // 2
            if letters[mid] <= target:
                l = mid + 1
            else:
                r = mid - 1

        return letters[l] if l < N else letters[0]