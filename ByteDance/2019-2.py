num = int(input())
for i in range(num):
    word = input()
    l = []

    if len(word) <=2 :
        print(word)
    
    else:
        l = list(word[0:2])
    

    position = 2
    while(position < len(word)):
        l.append(word[position])
        position += 1
        # print(l)
        if ((l[-1] == l[-2]) and (l[-2] == l [-3])):
            l = l[0:-1]
            # print("删除3:", l)
            continue
        if len(l) > 3:

            if ( (l[-3] == l[-4]) and (l[-1] == l[-2])):
                # print((l[[-3] == l[-4]]) and (l[-1] == l[-2]))
                l = l[0:-1]
                # print("删除4:", l)
                continue
        
    for j in l:
        print(j, end="")
    print()


