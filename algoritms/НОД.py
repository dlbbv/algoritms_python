a = int(input("Введите число: "))
b = int(input("Введите число: "))
x=[1,0]
if a>b: first,second = a,b
else: first,second = b,a
while a != 0 and b != 0:
    if a>b:
        cell = a // b
        a = a % b
        x.append(x[len(x)-2]-cell*x[len(x)-1])
    else:
        cell = b // a
        b = b % a
        x.append(x[len(x)-2]-cell*x[len(x)-1])
d = a + b
u = x[len(x)-2]
v = int((d-first*u)/second )  
print('('+str(first) +','+str(second)+') = '+str(first)+'*'+str(u)+'+'+str(second)+'*'+str(v)+' = '+str(d) )