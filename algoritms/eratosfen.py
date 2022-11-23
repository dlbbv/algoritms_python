from ast import Delete

def prost(x):
    x.insert(0,1)
    i=0
    while i < len(x):
        i+=1
        j=i+1
        while j < len(x):
            if x[j]%x[i]==0: del x[j]
            j+=1
    del x[0]
    return x

