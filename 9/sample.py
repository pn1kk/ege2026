import csv

data = []
with open('input9.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        st = []
        for i in row:
            st.append(int(i))
        data.append(st)

def cond1(x):
    ex = []
    for i in x:
        if i in ex:
            return False
        else:
            ex.append(i)
    return True

def cond2(x):
    a = x
    m1 = max(x)
    a.remove(m1)
    m2 = max(a)
    a.remove(m2)
    summax = m1 + m2
    summin = 0
    for i in a:
        summin += i
    if summax > summin:
        return False
    else:
        return True

ans = 0
for i in range(len(data)):
    if cond1(data[i]) and cond2(data[i]):
        ans += 1

print(ans)
