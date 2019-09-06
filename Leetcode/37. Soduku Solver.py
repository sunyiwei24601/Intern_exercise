class Solution():
    def solveSudoku(self, board):
        current_position = (0, -1)

        def back(current_position):
            x = current_position[0]
            y = current_position[1]
            if current_position == (8, 8):
                return True
            if y < 8:
                next_position = (x, y+1)
            else:
                next_position = (x+1, 0)
            
            x = next_position[0]
            y = next_position[1]
            if board[x][y] != '.':
                flag = back(next_position)
                return flag 
            else:
                row_list = [i for i in board[x] if i != '.']
                col_list = [i[y] for i in board if i[y] != '.' ]
                three_list = self.select_3(board, x, y)
                remain_numbers = self.find_remain(row_list, col_list, three_list)
                if remain_numbers:
                    for number in remain_numbers:
                        board[x][y] = str(number)
                        flag = back(next_position)
                        if flag:
                            return True
                        else:
                            board[x][y] = '.'
                    
                    return False
                else:
                    return False
        back(current_position)




    




    def find_remain(self, row_list, col_list, three_list):
        result = {str(i+1) for i in range(9)}
        return result - set(row_list) - set(col_list) - set(three_list)


    def select_3(self, board, x, y):
        x_start = (x // 3) * 3
        y_start = (y // 3) * 3
        x_end = x_start + 3
        y_end = y_start + 3
        l = []
        for i in range(x_start, x_end):
            for j in range(y_start, y_end):
                if board[i][j] == ".":
                    continue
                else:
                    l.append(board[i][j])
        return l

if __name__ == "__main__":
    s = Solution()
    board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    s.solveSoduku(board)
