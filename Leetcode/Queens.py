class Solution():
    def queens(self, nums):
        self.result_list = []


        def back( str_list):
            if len(str_list) == nums:
                self.result_list.append(str_list)
                return
            for current_queen in range(nums):
                flag = self.conflict(str_list, current_queen)
                if flag:
                    continue
                else:
                    # here we choose string + str() to make sure different back will not influence each other
                    # we can also use list ,and every time traceback, replicate a new list
                    back(str_list + str(current_queen))

        back('')
        return self.result_list

    def conflict(self, str_list, current_queen):
        len_ = len(str_list)
        for i in range(len_):
            #suppose every one in different rows, so the only two conflicts possible are
            #in the diagonal(rows difference equals col difference) or the same value(difference = 0)
            if int(str_list[i]) == current_queen or abs(int(str_list[i]) - current_queen) == (len_ - i):
                return True
        return False 

if __name__ == "__main__":
    s = Solution()
    print(len(s.queens(8)))