List = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
his = [[1 for j in i] for i in List ]

def search(List, his, i , j):
    if(i<0 or j<0 or i >= len(List) or j >= len(List[0]) ):
        return 0
    start_point = List[i][j]
    #确定未被搜索过
    if his[i][j] and start_point == 1:
        his[i][j] = 0
        left_search = search(List, his, i, j-1)
        right_search = search(List, his, i, j+1)
        down_search = search(List, his, i+1, j)
        up_search = search(List, his, i-1, j)
        return 1 + left_search + right_search + down_search + up_search
    else:
        his[i][j] = 0
        return 0
row = len(List)
col = len(List[0])
max_island = 0
for i in range(row):
    for j in range(col):
        temp = search(List, his, i, j)
        if temp > max_island:
            max_island = temp
            
print(max_island)
        
