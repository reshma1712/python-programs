def collatz():
    length = 0
    for i in range(13,1000000):
        n = i
        l = []
        while(n != 1):
            l.append(n)
            if n%2 == 0:
                n = n//2
            else :
                n = 3*n+1
        l.append(1)
        if(length<len(l)):
            j = i
            length = len(l)
    print(j)
collatz()
