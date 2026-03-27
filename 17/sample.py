with open('input17.txt', 'r') as file:
    data = list(map(int, file.read().split()))

x = min(data)
for i in data:
    try:
        if str(i)[-2:] == '18' and i > x:
            x = i
        else:
            pass
    except IndexError:
        pass

def cond1(a, b, c):
    if len(str(a)) == 5 or len(str(b)) == 5 or len(str(c)) == 5:
        return True
    else:
        return False

def cond2(a, b, c):
    if (a * b * c) % x == 0:
        return True
    else:
        return False

def gthr(a, b, c):
    if cond1(a, b, c) and cond2(a, b, c):
        return True
    else:
        return False

s = []
for i in range(len(data) - 2):
    if gthr(data[i], data[i+1], data[i+2]):
        s.append(data[i] * data[i+1] * data[i+2])

print(len(s), max(s))
