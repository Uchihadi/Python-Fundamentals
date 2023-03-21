def find_avg(list_num):
    result_sum=0
    for num in list_num:
        result_sum+=num
    result_avg=result_sum/len(list_num)
    print(result_avg)
    return result_avg

find_avg([5,8,5])