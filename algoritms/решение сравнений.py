import math

def solve_linear_congruence(a, b, m):
    m_start=m
    g = math.gcd(a, m)
    if g==1:
        if b % g:
            raise ValueError("Нет решений")
        a, b, m = a//g, b//g, m//g
        return pow(a, -1, m) * b % m, m
    elif g>1 and b%g==0:
        n=0
        a, b, m = a//g, b//g, m//g
        x = pow(a, -1, m) * b % m
        firt_x=x
        for i in range(g-1):
            print(f"Конкретное решение: x = {x+n}+{m_start}k")
            n=n+m
        return x+n, firt_x, g
    else:
        print("Нет решений")

def print_solutions(a, b, m):
    print(f"Исходное уравнение: {a}x = {b} (mod {m})")
    try:
        x, first_x, delitel = solve_linear_congruence(a, b, m)
    except ValueError:
        print("Нет решений")
    else:
        print(f"Конкретное решение: x = {x}+{m}k")
        print(f"Общее решение: x = {first_x}  (mod {int(m/delitel)})")

print("Введите данные для решения сравнения ax = b (mod m)")
a = int(input("Введите число a: "))
b = int(input("Введите число b: "))
m = int(input("Введите число m: "))
print_solutions(a, b, m)