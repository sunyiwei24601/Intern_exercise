class  Solution:
    def searchMatrix(self, matrix, target):
        m = len(matrix)
        if m:
            n = len(matrix[0])
        else:
            return False
        if not n:
            return False
        
        min_ = matrix[0][0]
        max_ = matrix[-1][-1]
        if target < min_ or target > max_:
            return False
        
        first_col = [i[0] for i in matrix] + [max_ + 1]
        last_col = [i[-1] for i in matrix] 
        first_row = self.search_first_bigger(first_col, target) + 1
        last_row = self.search_first_bigger(last_col, target)
        # print(last_row, first_row)
        rows = matrix[last_row: first_row]
        for row in rows:
            if self.search_index(row, target, 0, n - 1) != -1:
                return True 
        return False




    def search_first_bigger(self, l ,target):
        len_ = len(l)
        start = 0
        end = len_ - 1

        while(start <= end):
            if l[start] == target :
                return start
            if l[start] < target and l[start + 1] > target:
                break
            mid = (start + end) // 2
            if l[mid] == target:
                return mid 
            elif l[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return start


    def search_index(self, l, target, start, end):
        # print(start, end)
        if l[start] == target:
            return start
        if l[end] == target:
            return end
        if start >= end:
            return -1

        mid = (start + end) // 2
        if target == l[mid]:
            return mid
        if target > l[mid]:
            return self.search_index(l, target, mid + 1, end)
        else:
            return self.search_index(l, target, start, mid - 1)

if __name__ == "__main__":
    s = Solution()
    matrix=[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
    print(s.searchMatrix(matrix, 22))
    