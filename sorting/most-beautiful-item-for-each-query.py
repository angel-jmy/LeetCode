class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort(key = lambda x: (x[0], x[1]))
        N = len(items)
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
                return items[r][1]

        res = []
        for q in queries:
            res.append(find_beauty(q))

        return res
        