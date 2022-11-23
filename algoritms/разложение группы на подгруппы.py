import euler
def plus(m):
    x = list(range(0, m))
    d = [ x for x in range(1, m // 2 + 1) if m % x == 0 ]
    d.append(m)
    print(d)
    print("Всего групп: ", len(d))
    for k in range(len(d)):
        print("Группа ", k+1, ":")
        print("Подгрупп:",int(d[k]))
        print("Элементов в подгруппе: ",int(m/d[k]))
        n=0
        for i in range(d[k]):
            new_lst = []
            for j in range(len(x)):
                if x[j] % d[k] == 0:
                    new_lst.append(x[j]+n)
            print(new_lst)
            n+=1

def umnozh(m):
    E_m=euler.euler(m)
    x = list(range(1, m))
    d = [ x for x in range(1, E_m // 2 + 1) if E_m % x == 0 ]
    d.append(E_m)
    print("Всего групп: ", len(d))
    d_por=[]
    for j in range(len(d)):
        for i in range(len(x)):
            if (d[j]**x[i])%m==1:
                d_por.append(x[i])
                break
    print(d)
    print(d_por)
    for k in range(len(d)):
        print("Группа ", k+1, ":")
        print("Подгрупп:", E_m//d_por[k])
        print("Элементов в подгруппе: ",d_por[k])

        n=1
        n_n=1
        for i in range(E_m//d_por[k]):
            new_lst = []
            for j in range(d_por[k]):
                new_lst.append((((d[k]**n)%m)*n_n)%m)
                if n==d_por[k]:
                    n=1
                else:
                    n+=1
            n_n+=1
            print(new_lst)

m = int(input("Введите число m: "))
umnozh(m)
plus(m)
