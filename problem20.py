def factorial(n):
    if n == 1:
        return 1;
    else:
        return n*factorial(n-1)
def sum_of_digits(n):
    l = []
    while n >0:
        r = n%10
        l.append(r)
        n = n//10
    return sum(l)
n = factorial(100)
print(sum_of_digits(n))
