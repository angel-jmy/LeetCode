class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        timesF = [(a, l, i) for i, (a, l) in enumerate(times)]
        timesF.sort(key = lambda x: x[0])
        
        chairs = list(range(len(times)))
        taken = [] # Store the chair number and the leave time

        for a, l, i in timesF:
            while taken and a >= taken[0][0]:
                leave, num = heapq.heappop(taken)
                heapq.heappush(chairs, num)
                
            cur_num = heapq.heappop(chairs)
            if i == targetFriend:
                return cur_num

            heapq.heappush(taken, (l, cur_num))

