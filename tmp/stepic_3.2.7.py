a = input()
b = input()


def vpravo(st):
    """возвращает строку, сдвинутую на 1 вправо"""
    n_st = st[len(st)-1] + st[:-1]
    return n_st



if a == b:
    print (0)
else:
    flag = False
    for i in range(1, len(a)):
        a = vpravo(a)
        if a == b:
            flag = True
            break
    if flag:
        print(i)
    else:
        print(-1)
        
    
    
