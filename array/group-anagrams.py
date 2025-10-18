class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        counters = defaultdict(list)

        for item in strs:
            curr_tuple = tuple(sorted(item))

            counters[curr_tuple].append(item)
        
        return list(counters.values())