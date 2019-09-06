def get_input():
    s = input()
    s = s.split(" ")
    return [int(s[0]), int(s[1])]


num = int(input())
num_l = []
for i in range(num):
    num_l.append(get_input())
result = []
sorted_l = sorted(num_l)
max_y = sorted_l[-1][1]
result.append(sorted_l[-1])
for i in range(num - 2, -1, -1):
    if sorted_l[i][1] >= max_y:
        result.append(sorted_l[i])
        max_y = sorted_l[i][1]

for point in sorted(result):
    print(point[0], point[1])