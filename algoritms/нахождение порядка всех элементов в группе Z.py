import euler

def plus(m):
    print("Нахождение порядка всех элементов в группе Zm+:")
    x = list(range(0, m))
    d = [ x for x in range(1, m // 2 + 1) if m % x == 0 ]
    d.append(m)
    for j in range(len(x)):
        for i in range(len(d)):
            if (x[j]*d[i])%m==0:
                print("Порядок числа ", x[j], " равен ", d[i])
                break

def umnozh(m):
    print("Нахождение порядка всех элементов в группе Zm*:")
    Z_m=euler.euler(m)
    x = list(range(1, m))
    d = [ x for x in range(1, Z_m // 2 + 1) if Z_m % x == 0 ]
    d.append(Z_m)
    for j in range(len(x)):
        for i in range(len(d)):
            t=False
            if (x[j]**d[i])%m==1:
                print("Порядок числа ", x[j], " равен ", d[i])
                t=True
                break
        if t==False:
                print("Для числа ", x[j], " нет порядка")

m = int(input("Введите число m: "))
#plus(m)
umnozh(m)