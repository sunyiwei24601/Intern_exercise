class Solution:
    def removeDuplicates(self, nums) -> int:
        len_ = 1
        if nums :
            for i in range(1, len(nums)):
                if nums[i] == nums[i-1]:
                    nums.remove(nums[i])
                else:
                    len_ += 1
            #print(id(nums))
            return len_
        else:
            return 0

if __name__ == "__main__":
    s = Solution()
    nums = [1,2,2]
    
    print(s.removeDuplicates(nums))
    print(id(nums))