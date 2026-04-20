A = list(map(int, input().split()))
n = len(A)
i = 0
while i < n // 2:
    A[i], A[n - 1 - i] = A[n - 1 - i], A[i]
    i += 1
i = 0
while i < n:
    print(A[i], end=' ')
    i += 1
