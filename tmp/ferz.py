s = []
n = 8
for i in range(n):
    s.append(list(map(int, input().split())))

def ladya(x1,y1,x2,y2):
    if x1 == x2 or y1 == y2:
        return True
    else: return False


def slon(x1,y1,x2,y2):
    if abs(x1-x2) == abs(y1 - y2):
        return True
    else: return False


def is_fight(a,b):
    """
    проверяет, бьют ли друг друга два ферзя
    :param a: список координат
    :param b: список координат
    :return:  бьют ли друг друга два ферзя
    """
    flag = False
    x1 = a[0]
    y1 = a[1]
    x2 = b[0]
    y2 = b[1]
    if ladya(x1,y1,x2,y2) or slon(x1,y1,x2,y2):
        flag = True
    return flag

flag = False

for i in range(n):
    for k in range(i+1, n):
        if is_fight(s[i], s[k]):
            flag = True
            break
    if flag: break
if flag: print("YES")
else: print("NO")







