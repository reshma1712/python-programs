def sum_of_digits(n):
    l = []
    while n >0:
        r = n%10
        l.append(r)
        n = n//10
    return sum(l)
def large():
    v = 0
    for a in range(1,100):
        for b in range(1,100):
            n = a**b
            s = sum_of_digits(n)
            if (v < s):
                v = s
    print(v)
large()
