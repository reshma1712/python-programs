def distint_terms():
    l = []
    for i in range(2,101):
        l = l + power_check(i)
    l = set(l)
    return len(l)
def power_check(n):
    l = []
    for i in range(2,101):
        l.append(n**i)
    return l
print(distint_terms())
