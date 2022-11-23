import math

def solve_linear_congruence(a, b, m, kol):
    a_array=[]
    b_array=[]
    for i in range (kol):
        g = math.gcd(a[i], m[i])
        if b[i] % g:
            raise ValueError("Нет решений")
        a_array.append(a[i]//g)
        b_array.append(b[i]//g)
    return a_array, b_array

def solve_linear_congruence2(a, b, m):
    g = math.gcd(a, m)
    if b % g:
        raise ValueError("Нет решений")
    return pow(a, -1, m) * b % m

def print_solutions(a, b, m):
    try:
        x = solve_linear_congruence2(a, b, m)
    except ValueError:
        print("Нет решений")
    else:
        return x