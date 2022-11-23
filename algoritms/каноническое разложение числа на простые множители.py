def razl(num):
    otvet = str(num) + " = "
    list_simple = [0]
    list_stepen=[1]
    simple = 2
    while num > 1:
        if num % simple == 0:
            if simple != list_simple[len(list_simple)-1]:
                list_simple.append(simple)
                list_stepen.append(1)
            elif simple== list_simple[len(list_simple)-1]:
                list_stepen[len(list_stepen)-1]+=1
            num = num/simple
        else:
            simple += 1
    list_simple.pop(0)
    list_stepen.pop(0)
    for i in range(len(list_simple)):
        otvet = otvet+str(str(list_simple[i]) + "^" + str(list_stepen[i]) + " * ")
    otvet = otvet[:-2]
    print(otvet)
razl(int(input("Введите число для факторизации: ")))