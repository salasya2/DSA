class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:


        
        def dfs(row, col, i):
            if i == len(word):
                return True

            if (row >= len(board) or col >= len(board[0]) or row < 0 or col < 0 or board[row][col] == '#' or word[i] != board[row][col]):
                return False
            
            
            board[row][col] = '#'

            res = (dfs(row-1,col,i+1) or dfs(row, col - 1, i+1) or dfs(row+1,col,i+1) or dfs(row,col+1,i+1))

            board[row][col] = word[i]

            return res
        
        for i in range(len(board)):

            for j in range(len(board[0])):

                if dfs(i,j,0):
                    return True
        
        return False

        