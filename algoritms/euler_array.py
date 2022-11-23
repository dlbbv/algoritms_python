def findArray(m):
    b=m
    listb = list(range(1, b))
    listNew = []
    x=[1,0]
    i = 1
    while i<len(listb):
        a=listb[i]
        b=m
        while a != 0 and b != 0:
            if a>b:
                cell = a // b
                a = a % b
                x.append(x[len(x)-2]-cell*x[len(x)-1])
            else:
                cell = b // a
                b = b % a
                x.append(x[len(x)-2]-cell*x[len(x)-1])
        d = a + b
        if d==1: listNew.append(listb[i])
        i+=1
    return listNew



