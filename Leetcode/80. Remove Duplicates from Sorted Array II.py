class Solution:
    def removeDuplicates(self, nums) -> int:
        post = 2
        len_ = len(nums)
        

        for curr in range(2, len_):
            if nums[curr] != nums[post - 2]:
                nums[post] = nums[curr]
                post += 1
        
        return post

if __name__ == "__main__":
    s = Solution()
    print(s.removeDuplicates([1,1,1,1,2,2,3,3]))
        