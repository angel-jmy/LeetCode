class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        INF = float('inf')
        cost = [INF] * n
        cost[src] = 0
        for _ in range(k + 1):  # at most k stops => k+1 edges
            nxt = cost[:]       # relax using previous layer only
            for u, v, w in flights:
                if cost[u] != INF and cost[u] + w < nxt[v]:
                    nxt[v] = cost[u] + w
            cost = nxt
        return -1 if cost[dst] == INF else cost[dst]

        