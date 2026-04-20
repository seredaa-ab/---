A = list(map(int, input().split()))
odds = []
for x in A:
    if x % 2 != 0:
        odds.append(x)
if len(odds) == 0:
    print(0)
else:
    print(min(odds))