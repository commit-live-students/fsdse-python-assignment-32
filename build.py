def solution(list_of_integers):
    sum_numbers= 0
    for k in list_of_integers:
        sum_numbers = sum_numbers+k
    return sum_numbers

output = solution([1,2,3,4,5])
print output
