from itertools import permutations

letters = ['k', 'a', 'r', 'p', 'i']
vowels = ['a', 'i']
words = [''.join(p) for p in permutations(letters)]

def conds(x):
    if x[0] == 'r' or x[-1] == 'r':
        return False
    for i in range(len(x[:-1])):
        if x[i] in vowels and x[i+1] in vowels:
            return False
    return True

ans = 0
for word in words:
    if conds(word) == True:
        ans += 1

print(ans)
