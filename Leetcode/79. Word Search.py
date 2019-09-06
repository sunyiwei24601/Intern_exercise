class Solution:
    def exist(self, board, word):
        rows = len(board)
        if rows:
            cols = len(board[0])
        memo = [[1]*cols for i in range(rows)]

        def exist_word(matrix, memo, word, row, col):
            if len(word) == 0:
                return 1
            if  row >= rows or row < 0   or col >= cols or col < 0 or matrix[row][col] != word[0] or  not memo[row][col] :
                return -1
            else:
                memo[row][col] = 0
                left = exist_word(matrix, memo, word[1:], row, col + 1)
                if left == 1: return 1
                right = exist_word(matrix, memo, word[1:], row, col - 1)
                if right == 1 : return 1
                up = exist_word(matrix, memo, word[1:], row - 1, col)
                if up == 1 : return 1
                down = exist_word(matrix, memo, word[1:], row + 1, col)
                if down == 1 : return 1
                memo[row][col] = 1
                return -1
                
        result = -1
        for i in range(rows):
            for j in range(cols):
                
                result = exist_word(board,  memo, word, i, j)
                if result == 1:
                    return True
        return False
    
    def exist2(self, board, word):
        rows = len(board)
        if rows:
            cols = len(board[0])
        memo = [[1]*cols for i in range(rows)]

        def exist_word(matrix, memo, word, row, col):
            if len(word) == 0:
                return 1
            if  row >= rows or row < 0   or col >= cols or col < 0 or matrix[row][col] != word[0] or  not memo[row][col] :
                return -1
            else:
                memo[row][col] = 0
                left = exist_word(matrix, memo, word[1:], row, col + 1)
                right = exist_word(matrix, memo, word[1:], row, col - 1)
                up = exist_word(matrix, memo, word[1:], row - 1, col)
                down = exist_word(matrix, memo, word[1:], row + 1, col)
                return max(left, right, up, down)
        result = -1
        for i in range(rows):
            for j in range(cols):
                
                result = exist_word(board,  memo, word, i, j)
                if result == 1:
                    return True
        return False

if __name__ == "__main__":
    s = Solution()
    board = [["a","a","a","a"],
    ["a","a","a","a"],["a","a","a","a"],["a","a","a","a"],["a","a","a","b"]]

    print(s.exist(board, "aaaaaaaab"))

        