from ast import Continue
import euqlid
import sravn

def anySol(koef_m):
    sol=True
    for i in range(kol):
        for j in range(i+1,kol):
            if euqlid.nod(koef_m[i],koef_m[j])==1:
                Continue
            else:
                sol=False
    return sol

def reshenie(koef_a,koef_b,koef_m, kol):
    koef_a, koef_b = sravn.solve_linear_congruence(koef_a,koef_b,koef_m,kol)
    M0=1
    for i in range (kol):
        M0*=koef_m[i]
    Mi_array=[]
    for i in range (kol):
        Mi_array.append(int(M0/koef_m[i]))
    x_array=[]
    for i in range (kol):
        x_array.append(sravn.print_solutions(Mi_array[i],koef_b[i],koef_m[i]))
    x=0
    for i in range (kol):
        x+=Mi_array[i]*x_array[i]
    x=x%M0
    print(f"Общее решение: x = {x}  (mod {M0})")
    print(f"Конкретное решение: x = {x}")

koef_a=[]
koef_b=[]
koef_m=[]
kol=int(input("Введите кол-во сравнений:"))
for i in range (kol):
    print("Для уравнения ax=b(mod m) введите данные для уравнения " + str(i+1) + ":")
    koef_a.append(int(input("Введите значение a: ")))
    koef_b.append(int(input("Введите значение b: ")))
    koef_m.append(int(input("Введите значение m: ")))

if(anySol(koef_m)):
    reshenie(koef_a,koef_b,koef_m, kol)
else:
    print("Нет решений")

