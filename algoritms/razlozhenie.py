def razl(num):
    list_simple = [0]
    simple = 2
    while num > 1:
        if num % simple == 0:
            if simple != list_simple[len(list_simple)-1]:
                list_simple.append(simple)
            num = num/simple
        else:
            simple += 1
    list_simple.pop(0)
    return list_simple