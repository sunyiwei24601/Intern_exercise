

def search_target(nums, target):
    n = len(nums)
    upper_bound = n - 1
    down_bound = 0
    current_i = 0
    while(nums[current_i] != target):
        if nums[current_i] > target:
            temp = int((current_i + down_bound)/2)
            upper_bound = current_i
            current_i = temp
        elif nums[current_i] < target:
            temp = int((current_i + upper_bound)/2)
            down_bound = current_i
            current_i = temp
    return current_i
    

def search(nums, target):
    left_min = nums[0]
    right_max = nums[-1]
    n = len(nums)
    upper_bound = n -1
    down_bound = 0
    current_i = int(n/2)
    while(nums[current_i-1] <= nums[current_i] and nums[current_i] <= nums[current_i+1]):
        if nums[current_i] >= left_min:
            temp = int((current_i + upper_bound)/2)
            down_bound = current_i
            current_i = temp
        else:
            temp = int((current_i+down_bound)/2)
            upper_bound = current_i
            current_i = temp
    if nums[current_i] >= left_min:
        current_i += 1
    #     return current_i + 1
    # else:
    #     return current_i
    if target > left_min:
        search_list = nums[:current_i]
        result = search_target(search_list, target)
    else:
        search_list = nums[current_i:]
        result = search_target(search_list, target)
        result += current_i
    return result

print(search([4,5,6,7,8,9,10,0,1,2], 8 ))
