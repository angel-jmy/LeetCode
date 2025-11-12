class Solution:
    def resultsArray(self, queries: List[List[int]], k: int) -> List[int]:
        res = []
        distances = []
        counter = 0
        for x, y in queries:
            dist = abs(x) + abs(y)
            counter += 1

            if counter < k:
                heapq.heappush(distances, -dist)
                res.append(-1)
            elif counter == k:
                heapq.heappush(distances, -dist)
                res.append(-distances[0])
            else:
                if -dist <= distances[0]:
                    res.append(-distances[0])
                    counter -= 1
                else:
                    heapq.heappushpop(distances, -dist)
                    res.append(-distances[0])
                    counter -= 1

        return res