class Solution:
    def searchMatrix(self, Matrix, target):
        m = len(Matrix)
        if m : 
            n = len(Matrix[0])
        else:
            return False
        if n == 0 : return False
        max_ = Matrix[-1][-1]
        min_ = Matrix[0][0]

        if target > max_ or target < min_:
            return False

        first_col_list = [i[0] for i in Matrix]
        first_col_list += [max_ + 1 ]
        r = self.search_row(first_col_list, target, 0, m)
        index = self.search_index(Matrix[r], target, 0, n - 1)
        print(r, index)

    def search_index(self, l, target, start, end):
        print(start, end)
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
    
    def search_row(self, l, target, start, end):
        if l[start] <= target and l[end] > target and start - end == -1:
            return start

        mid = (start + end) // 2
        print(start, mid, end, l[mid])
        
        if target >= l[mid]:
            return self.search_row(l, target, mid, end)
        else:
            return self.search_row(l, target, start, mid)


if __name__ == "__main__":
    s = Solution()
    matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
    print(s.searchMatrix(matrix, 13))