def threeSum(nums):
    result = []
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            num1 = nums[i]
            num2 = nums[j]
            
            if -(num1 + num2) in nums[j+1:]:
                print([num1, num2, -(num1+num2)])
                print(-(num1+num2), nums[j+1:])
                
                result.append([num1, num2, -(num1+num2)])
    rr = [sorted(i) for i in result]
    ss = []
    for r in rr:
        if not r in ss:
            ss.append(r)
    return ss

print(threeSum([-1,0,1,2,-1,-4]))