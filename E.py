A = list(map(int, input().split()))
i = 0
while i < len(A) and A[i] <= 0:
    i += 1
if i < len(A):
    print(i)
else:
    print(-1)