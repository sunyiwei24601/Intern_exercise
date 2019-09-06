


def check_out(people_num, people_score, prizes):
    if people_score[0] > people_score[1]:
        prizes[0] = people_score[1] + 1
    if people_score[0] > people_score[-1]:
        if prizes[-1] > prizes[0]:
            prizes[0] = prizes[-1] + 1


    for i in range(1,people_num - 1):
        if (people_score[i] > people_score[i-1]):
            temp_prize = prizes[i-1] + 1
            if temp_prize > prizes[i]:
                prizes[i] = temp_prize
        if (people_score[i] > people_score[i+1]):
            temp_prize = prizes[i+1] + 1
            if temp_prize > prizes[i]:
                prizes[i] = temp_prize
    if people_score[-1] > people_score[-2]:
        prizes[-1] = prizes[-2] + 1
    if people_score[-1] > people_score[0]:
        if prizes[0] >= prizes[-1]:
            prizes[-1] = prizes[0] + 1

    return sum(prizes),prizes




num = int(input())


for i in range(num):
    people_num = int(input())
    people_score_input = input().split(" ")
    people_score = [int(j) for j in people_score_input]
    prizes = [1 for ss in range(people_num)]
    sum_past = 0
    sum_new = sum(prizes)
    while(sum_new != sum_past):
        sum_past = sum_new
        sum_new,prizes = check_out(people_num,people_score,prizes)
    print(sum_new)

    
    







