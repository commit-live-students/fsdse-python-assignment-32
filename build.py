from functools import reduce

def solution(list_of_integers):
    '''
    Enter your code here
    '''
    sum_numbers = reduce((lambda x, y:x+y), list_of_integers)
    return sum_numbers

print(solution([1,2,3,4,5,6,7]))
