class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low = 0
        high = (len(matrix) * len(matrix[0])) - 1
        

        while low <= high:
            mid = (low + high) // 2
            #tells us how many rows we have passed
            row = mid // len(matrix[0])
            #tells us how far into the row we are (therefore, cols)
            col = mid % len(matrix[0])
            if target > matrix[row][col]:
                low = mid + 1
            elif target < matrix[row][col]:
                high = mid - 1
            else:
                return True
        return False
