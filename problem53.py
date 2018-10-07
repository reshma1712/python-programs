def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact*i
    return fact
def combinatorics():
    count = 0
    for i in range(1,101):
        for r in range(1,i+1):
            if(factorial(i)/(factorial(r)*factorial(i-r)) >1000000):
                count = count+1
    print(count)
combinatorics()
