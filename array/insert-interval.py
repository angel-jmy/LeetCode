class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """

        N = len(intervals)
 
        res = []
        res_size = 0
        inserted = False
        
        for i in range(N):
            start, end = intervals[i][0], intervals[i][1]
        
            if not inserted:
        
                if end < newInterval[0]:
                    res.append(intervals[i])
                    res_size += 1
                    continue
        
                if start > newInterval[1]:
                    res.append(newInterval)
                    res = res + intervals[i:]
                    return res
        
                else:
                    left = min(start, newInterval[0])
                    right = max(end, newInterval[1])
                    
                    res.append([left, right])
                    inserted = True
                    res_size += 1
                    continue
            
            else:
                if end <= res[res_size - 1][1]:
                    continue
                if res[res_size - 1][0] <= start <= res[res_size - 1][1] and end > res[res_size - 1][1]:
                    res[res_size - 1] = [res[res_size - 1][0], end]
        # elif start > res[res_size - 1][1]:
                else:
                    res = res + intervals[i:]
                    return res
        
        if not inserted:
            res.append(newInterval)

        return res
