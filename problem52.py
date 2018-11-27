def sort_list(n):
    l = []
    while n >0:
        r = n%10
        l.append(r)
        n = n//10
    return sorted(l)
def no_of_digits(n):
    i = 0
    while n >0:
        r = n%10
        i = i+1
        n = n//10
    return i
def multiples():
    for i in range(1,1000000):
        n = no_of_digits(i)
        n1 = no_of_digits(i*2)
        n2 = no_of_digits(i*3)
        n3 = no_of_digits(i*4)
        n4 = no_of_digits(i*5)
        n5 = no_of_digits(i*6)
        if (n == n1 and n1 == n2 and n1 == n3 and  n1 == n4 and n1 == n5):
            s1 = sort_list(i*2)
            s2 = sort_list(i*3)
            s3 = sort_list(i*4)
            s4 = sort_list(i*5)
            s5 = sort_list(i*6)
            if (s1 == s2 and s1 == s3 and  s1 == s4 and s1 == s5):
                print(i)
                break
multiples()
