def amicablePairs():
    # ADD YOUR CODE HERE
    list = []
    i = 1
    while i <= 10000 :
        a = divisors_sum(i)
        b = divisors_sum(a)
        if (b == i and i!= a and i < a):
            list.append(i)
            list.append(a)
        i+=1
    return sum(list)
def divisors_sum(num):
    i = 1
    sum = 0
    for i in range( 1,num):
        if num % i == 0:
           sum = sum + i
    return sum
print(amicablePairs())
