class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            for j in range(9):
                curr = board[i][j]
                if curr != '.' and curr in [board[i][k] for k in range(9) if k != j]:
                    return False
                if curr != '.' and curr in [board[k][j] for k in range(9) if k != i]:
                    return False
                if curr != '.':
                    for x in range(3):
                        for y in range(3):
                            newCurr = board[i - i % 3 + x][j - j % 3 + y]
                            if i - i % 3 + x != i or j - j % 3 + y != j:
                                if newCurr == curr:
                                    return False
                            
    
        return True
                            