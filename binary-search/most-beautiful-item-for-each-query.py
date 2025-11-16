class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort(key = lambda x: (x[0], x[1]))
        N = len(items)
        pref_max = [0] * N
        pref_max[0] = items[0][1]
        for i in range(1, N):
            pref_max[i] = max(pref_max[i - 1], items[i][1])

        def find_beauty(target):
            l, r = 0, N - 1
            while l <= r:
                mid = l + (r - l) // 2
                if items[mid][0] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            if r < 0:
                return 0
            else:
                return pref_max[r]

        res = []
        for q in queries:
            res.append(find_beauty(q))

        return res
        