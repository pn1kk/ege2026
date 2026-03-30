f = open('24.txt', 'r')
data = f.read()
data1 = data
it1, it2 = 'PR', 'ST'
s1 = data.replace(it1, it1[0] + ' ' + it1[1])
s2 = data1.replace(it2, it2[0] + ' ' + it2[1])

ans1 = max(s1.split(), key = len)
ans2 = max(s2.split(), key = len)

print(len(ans1), ans1)
print(len(ans2), ans2)
