def euler(n):
    r = n
    i = 2
    while i*i <= n:
        if n % i == 0:
            while n % i == 0:
                n //= i
            r -= r//i
        else:
            print(i)
            i += 1
    if n > 1:
        r -= r//n
    return r

n = int(input("Введите число: "))
print(euler(n))

