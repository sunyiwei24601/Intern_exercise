class Solution:
    def spiralOrder(self, matrix):
        m = len(matrix)
        if m:
            n = len(matrix[0])
        else:
            return []
        
        # [[1]*n]*m is wrong ,since they use m reference of [1]*n
        mem_matrix = [[1] * n for i in range(m)]
        result = []
        
        col, row = 0, 0
        result.append(matrix[row][col])
        mem_matrix[row][col] = 0
        def search_direction(row, col, right, down, matrix, mem_matrix, result):
            while (col + right)>= 0 and (col + right) < n and (row + down) < m and mem_matrix[row + down][col + right]:
                col += right
                row += down
                result.append(matrix[row][col])
                mem_matrix[row][col] = 0
            return row, col
        
        while len(result) < m * n :
            #search right,down,ledf,up
            row, col = search_direction(row, col, 1, 0, matrix, mem_matrix, result)
            row, col = search_direction(row, col, 0, 1, matrix, mem_matrix, result)
            row, col = search_direction(row, col,-1, 0, matrix, mem_matrix, result)
            row, col = search_direction(row, col, 0, -1, matrix, mem_matrix, result)
        return result

if __name__ == "__main__":
    s = Solution()
    print(s.spiralOrder([
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]))
       
                    



        