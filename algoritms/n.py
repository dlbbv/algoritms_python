from ast import Continue
import euqlid

def anySol(koef_m):
    sol=True
    for i in range(kol):
        for j in range(i+1,kol):
            if euqlid.nod(koef_m[i],koef_m[j])==1:
                Continue
            else:
                sol=False
    return sol

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
    print("Есть решения")
else:
    print("Нет решений")

