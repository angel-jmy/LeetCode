class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        g = defaultdict(list)
        for start, end, t in times:
            g[start].append((end, t))

        # Shortest-known times from k; 1-indexed
        mintimes = [float('inf')] * (n + 1)
        mintimes[k] = 0

        # Min-heap of (current_best_time, node)
        pq = [(0, k)]
        while pq:
            time_u, u = heapq.heappop(pq)
            # Skip stale entries
            if time_u > mintimes[u]:
                continue

            for v, w in g[u]:
                new_time = time_u + w
                if new_time < mintimes[v]:
                    mintimes[v] = new_time
                    heapq.heappush(pq, (new_time, v))

        ans = max(mintimes[1:])  # ignore index 0
        return -1 if ans == float('inf') else ans

        # INF = float('inf')
        # dist = [INF] * (n + 1)   # nodes are 1..n
        # dist[k] = 0

        # # Relax all edges up to n-1 times
        # for _ in range(n - 1):
        #     updated = False
        #     # IMPORTANT: iterate over the original edge list (no graph needed)
        #     for u, v, w in times:
        #         if dist[u] != INF and dist[u] + w < dist[v]:
        #             dist[v] = dist[u] + w
        #             updated = True
        #     if not updated:
        #         break  # early stop if no change this round

        # ans = max(dist[1:])  # ignore index 0
        # return -1 if ans == INF else ans
