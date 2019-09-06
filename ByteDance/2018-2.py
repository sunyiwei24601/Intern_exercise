num = int(input())
s = input().split(' ')
s = [int(i) for i in s]
max_result = 0
for i in range(num):
    center = s[i]
    
    right_interval = 0
    while (i + right_interval + 1) <= (num - 1) :
        
        if s[i + right_interval + 1] >= center:
            right_interval += 1
        else:
            break
    left_interval = 0
    while ((i - left_interval - 1) >= 0):
        
        if (s[i - left_interval - 1] >= center):
            left_interval += 1
        else:
            break
    print(left_interval, right_interval)
    temp_max = center * sum(s[i-left_interval:i+right_interval+1])
    print(temp_max)
    if temp_max > max_result:
        max_result = temp_max
print(max_result)