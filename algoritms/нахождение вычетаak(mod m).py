def vichet(a, k, m):
    newk=k%(m-1)
    newa=(a**newk)-(m*((a**newk)//m))
    print(f"Решение уравнения {a}^{k} (mod {m}) = {newa} (mod {m}) = {newa%m}")

print("Для решения уравнения a^k(mod m) введите данные:")
vichet(int(input("Введите значение a: ")), int(input("Введите значение k: ")), int(input("Введите значение m: ")))