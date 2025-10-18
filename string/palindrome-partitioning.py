class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        N = len(s)

        def isPalindrome(l, r):
            while l <= r:
                if s[l] != s[r]:
                    return False
                
                l += 1
                r -= 1

            return True


        def backtrack(path, idx):
            if idx == N:
                res.append(path[:])
                return 

            for i in range(idx, N):
                path.append(s[idx:i + 1])

                if isPalindrome(idx, i):
                    backtrack(path, i + 1)
                    path.pop()
                
                else:
                    path.pop()
                    continue

                

                  
        backtrack([], 0)

        return res


    