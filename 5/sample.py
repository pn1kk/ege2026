def alg(x):
    if x%2 == 0:
        return int('10' + bin(x)[2:], 2)
    else:
        return int('1' + bin(x)[2:] + '01', 2)

s = []
for i in range(12):
    s.append(alg(i+1))

print(max(s))
