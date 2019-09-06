class Solution:
    def searchRange(self, nums, target: int):
        
        def search_left(nums, start, end, target):
            mid = (start + end) // 2
            if start == end:
                if nums[start] == target:
                    return start
                else: 
                    return -1
            if nums[end] == target:
                if nums[mid] == target:
                    return search_left(nums, start, mid, target)
                else:
                    return search_left(nums, mid + 1, end, target)
            elif nums[mid] == target:
                return search_left(nums, start, mid, target)
            else:
                return max(search_left(nums, start, mid, target),
                            search_left(nums, mid + 1, end, target))
        
if __name__ == "__main__":
    s = Solution()
    s.searchRange([5,7,7,8,8,10], 8)