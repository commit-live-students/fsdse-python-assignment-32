def solution(list_of_ints):
    sum_no = 0
    for k in range(0,len(list_of_ints)):
        sum_no = sum_no + list_of_ints[k]
    return sum_no

print solution([5,4,6])
