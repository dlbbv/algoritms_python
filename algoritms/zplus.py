def plus(m):
    print("Нахождение порядка всех элементов в группе Zm+:")
    plus_array = []
    x = list(range(0, m))
    d = [ x for x in range(1, m // 2 + 1) if m % x == 0 ]
    d.append(m)
    for j in range(len(x)):
        for i in range(len(d)):
            if (x[j]*d[i])%m==0:
                plus_array.append([x[j], d[i]])
                break
    return plus_array