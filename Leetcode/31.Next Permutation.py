class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        len_ = len(nums)
        if len_ == 1:
            print(nums)
            return nums
        turning_digits = -1
        # from end to start ,find the point number getting smaller
        for i in range(len_-2,-1,-1):
            if nums [i] < nums[i+1]:
                turning_digits = i
                break
        # if the list is all descending ,reverse it
        if turning_digits == -1 :
            result = nums.reverse()
            return result
        
        # find the number just bigger than turning number
        turning_number = nums[i]
        for j in range(i+1, len_):
            if nums[j] <= turning_number:
                j -= 1
                break
        nums[turning_digits] = nums[j]
        nums[j] = turning_number

        c = nums[i+1:]
        c.reverse()
        nums[i+1:] = c
        
        print(nums)

if __name__ == "__main__":
    s = Solution()
    s.nextPermutation([1,5,1])
        


    
        