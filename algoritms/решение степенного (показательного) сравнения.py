import pervoobr
import obr
import euqlid
import sravn
import euler

#индекс числа
def index(a,b,m):
    x=0
    while (a**x)%m!=b:
        x+=1
        if x==10000:
            break
    if x==10000:
        return("Нет решений")
    else:
        return x

def resh1(a,k,b,m):
    if a!=1:
        obra=obr.mulinv(a,m)
        a,b=a*obra,b*obra
    a,b=a%m,b%m
    b=index(pervoobr.pervoobr(m),b,m)
    a=k
    j=m-1
    d=euqlid.nod(a,j)
    if b%d==0:
        a,b,t=a/d,b/d,j/d
        if a!=1:
            obra_=obr.mulinv(a,t)
            a,b=a*obra_,b*obra_
        a,b=a%t,b%t
        print("x= " + str(pervoobr.pervoobr(m)) + "^(" + str(int(b)) + " + " + str(int(t)) + "k)")
    else:
        print("Нет решений")
    
def resh2(a,b,m):
    b=index(pervoobr.pervoobr(m),b,m)
    a=index(pervoobr.pervoobr(m),a,m)
    x = sravn.print_solutions(a,b,euler.euler(m))
    print(f"x= {x} + {euler.euler(m)}k")
    
print("Введите 1, чтобы решить уравнения вида ax^n=b(mod m)")
print("Введите 2, чтобы решить уравнения вида a^x=b(mod m)")
chislo=int(input("Введите число: "))
if chislo==1:
    print("Для уравнения ax^n=b(mod m)")
    a=int(input("Введите число a: "))
    k=int(input("Введите число n: "))
    b=int(input("Введите число b: "))
    m=int(input("Введите число m: "))
    resh1(a,k,b,m)
elif chislo==2:
    print("Для уравнения a^x=b(mod m)")
    a=int(input("Введите число a: "))
    b=int(input("Введите число b: "))
    m=int(input("Введите число m: "))
    resh2(a,b,m)
else:
    print("Вы ввели неверное число")