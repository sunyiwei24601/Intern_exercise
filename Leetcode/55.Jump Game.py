class Solution:
    def canJump(self, nums) -> bool:
        memo = [0] * len(nums)
        memo[-1] = 1
        len_ = len(nums)


        for i in range(len_-2, -1, -1):

            furthest_position = min(len_ -1, i + nums[i])
            for j in range(i, furthest_position + 1):
                if memo[j] == 1:
                    memo[i] = 1
                    break
            if not memo[i]:
                memo[i] = -1
        
        if memo[0] == -1:
            return False
        else:
            return True

    def canJump2(self,nums):
        len_ = len(nums)
        last_position =  len_ - 1
        for i in range(len_ - 1, -1, -1):
            if nums[i] + i >= last_position:
                last_position = i
        if last_position == 0:
            return True
        else:
            return False





if __name__ == "__main__":
    s = Solution()
    print(s.canJump2([3,2,1,1,4]))