n = int(input())
data = []
for i in range(n):
    a, b = map(int, input().split())
    data.append([a, b])

data.sort(key=lambda x: (x[0], x[1]))

stid = []
for i in data:
    if i[0] not in stid:
        stid.append(i[0])

mxsols = 0
idx = 0

def podr(x):
    cur = maxlen = 1
    for i in range(1, len(x)):
        if x[i] == x[i-1] + 1:
            cur += 1
        else:
            cur = 1
        maxlen = max(maxlen, cur)
    return maxlen

index = 0
for st_id in stid:
    pr = []
    while index < n and data[index][0] == st_id:
        if data[index][1] not in pr:
            pr.append(data[index][1])
        index += 1

    pr.sort()

    if podr(pr) > mxsols:
        mxsols = podr(pr)
        idx = st_id

print(idx, mxsols)
