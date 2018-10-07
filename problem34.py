def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact*i
    return fact
def sum_factorial(n):
    s = 0
    while (n > 0):
        r = n%10
        s = s+factorial(r)
        n = n//10
    return s
def sum():
    s = 0
    for i in range(10,1000000):
        if(sum_factorial(i) == i):
            s = s+i
    print(s)
sum()
