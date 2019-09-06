class Solution:
    def search(self, nums, target: int) -> int:
        
        def search_num(nums, start, end, target):
            found = -1
            if not nums:
                return -1
            elif nums[start] == target:
                return start
            elif start < end:
                mid = (start + end) // 2
                if nums[start] > nums[end]:
                    found = max(search_num(nums, start, mid, target),
                                search_num(nums, mid + 1, end,target))
                elif nums[mid] <= target:
                    found = search_num(nums, mid, end, target)
                else:
                    found = search_num(nums, start, mid-1, target)
            
            return max(found, -1)

        return search_num(nums, 0, len(nums) - 1, target)

if __name__ == "__main__":
    s = Solution()
    print(s.search([4,5,6,0,1,2,3], 0))