def m(x):
    s = []
    for i in range(2, int(x**0.5 + 1)):
        if x % i == 0 and i not in s:
            s.append(i)
            if x//i not in s:
                s.append(x//i)
    if s == []:
        return 0
    else:
        return s[0] + s[-1]

x = 220000
cnt = 0
while cnt < 5:
    x += 1
    if str(m(x))[-1] == '4':
        print(x, m(x))
        cnt += 1
