def fizz_buzz(upper_bound):
    result = []
    for index in range(upper_bound):
        count = index+1
        if count %3 == 0:
            result.append('fizz')
        else: 




            result.append(str(count))
    return result