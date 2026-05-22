f = open('26_5363.txt').readlines()
s = []
n = int(f[0].split()[0])
l = int(f[0].split()[1])
for i in range(1, len(f) - 1):
    s.append(list(map(int, f[i].split())))

s.sort(key = lambda x: (x[1], x[0]))
dp = [1]
for i in range(1, len(s)):
    j = -1
    for k in range(i):
        if s[k][1] <= s[i][0]:
            j = k
    if j == -1:
        dp += [dp[i-1]]
    else:
        dp += [max(dp[i-1], 1 + dp[j])]

mx = dp[-1]
mn = s[-1][0]

for i in range(len(dp)):
    if dp[i] == mx:
        mn = min(mn, s[i][0])

print(mx, mn)
