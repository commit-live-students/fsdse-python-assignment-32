def solution(list_of_integers):
    sum_numbers = 0
    for i in range(0, len(list_of_integers)):
        print ("I ", list_of_integers[i])
        print (sum_numbers, "Hii")
        sum_numbers = sum_numbers + list_of_integers[i]
        print sum_numbers
    print sum_numbers
    return sum_numbers
