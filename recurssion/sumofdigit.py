def sum_of_digits(n):
    assert n >=0 and int(n) == n,"Please enter a postive integer"
    if n in [0,1,2,3,4,5,6,7,8,9]:
        return n
    else:
        return n%10+sum_of_digits(n//10)


print(sum_of_digits(-10))