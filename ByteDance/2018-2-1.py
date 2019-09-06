num = int(input())
s = input().split(" ")
search_list = [int(i) for i in s]
search_n = int(input())


def get_search():
    s = input().split(" ")
    s = [int(i) for i in s]
    return s


for i in range(search_n):
    search = get_search()
    start = search[0]
    end = search[1]
    k = search[2]
    count = 0
    for i in search_list[start - 1:end]:
        if i == k:
            count += 1
    print(count)




