class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        #created hash set
        path = set()
        
        def dfs(row, col, i):
        #word[i]; i equals each letter
        #board[row][col]; equals each individual letter
            if i == len(word):
                return True
            if (row < 0 or col < 0 or row >= rows or col >= cols or board[row][col] != word[i] or (row,col) in path):
                return False
            
            path.add((row, col))
            #4 cases for trying to form word(can only be directly horizontal or vertical to current element)
            res = (dfs(row+1, col, i+1) or dfs(row-1, col, i+1) or dfs(row, col+1, i+1) or dfs(row, col-1, i+1))
            path.remove((row, col))
            return res
        
        #running through entire board    
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0): 
                    return True
        return False 
