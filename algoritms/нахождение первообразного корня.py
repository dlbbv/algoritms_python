from ast import Continue
import euler_array
import razlozhenie
import razlozhenie_all
import eratosfen

def pervoobr(m):
    arrayA=euler_array.findArray(m)
    fm=len(arrayA)+1
    arrayMnozh=razlozhenie.razl(fm)
    arrayStep = arrayMnozh
    arrayAll = razlozhenie_all.razl(fm)
    if(len(arrayAll)>2):
        for i in range (len(arrayAll)-1):
            arrayStep.append(arrayAll[i]*arrayAll[i+1])
    massprost=eratosfen.prost(arrayA)
    for i in range (len(massprost)):
        trueA=True
        for j in range (len(arrayStep)):
            if (massprost[i]**arrayStep[j])%m!=1:
                Continue
            else:
                trueA=False
                break
        if trueA:
            print(f"Первообразный корень равен {massprost[i]}")
            arrayStepU = list(range(0, m-1))
            arrayU = []
            for k in range (m-1):
                if (massprost[i]**arrayStepU[k])<m:
                    arrayU.append(massprost[i]**arrayStepU[k])
                else:
                    arrayU.append((massprost[i]**arrayStepU[k])-(m*((massprost[i]**arrayStepU[k])//m)))
            print(f"Приведенная системы вычетов: U({m}) = {arrayU}")
            break
        if i+1==len(massprost):
            print("Первообразного корня нет")

pervoobr(int(input("Введите число m: ")))
