def solution(list_of_integers):
    '''
    Enter your code here
    '''
    sum_numbers = 0
    for k in range(0,len(list_of_integers)):
        sum_numbers = sum_numbers + list_of_integers[k]

    return sum_numbers

solution([1,6,3])
