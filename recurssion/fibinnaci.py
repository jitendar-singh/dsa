def fibinacci(n):
    assert n >= 0 and int(n) == n,"Fibonacci number cannot be negative or non Integer"
    if n in [0,1]:
        return n
    else:
        return fibinacci(n-1) + fibinacci(n-2)
    
print(fibinacci(5))