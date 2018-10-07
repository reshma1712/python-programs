def sum_of_fifth():
    l = []
    for i in range(1000,1000000):
        if armstrong(i) == i:
            l.append(i)
    return sum(l)
def armstrong(n):
    l = []
    while(n>0):
        r = n%10
        l.append(r**5)
        n = n//10
    return sum(l)
print(sum_of_fifth())
