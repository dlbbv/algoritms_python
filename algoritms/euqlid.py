def nod(a,b):
    x=[1,0]
    if a>b: first,second = a,b
    else: first,second = b,a
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
    return d