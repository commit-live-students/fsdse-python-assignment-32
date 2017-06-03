from functools import reduce
#Note - The function reduce(func, seq) continually applies the function func() to the sequence seq. It returns a single value.

def solution(list_of_integers):
    '''
    Enter your code here
    '''
    sum_numbers = reduce((lambda x, y:x+y), list_of_integers)
    return sum_numbers

print(solution([1,2,3,4,5,6,7]))
