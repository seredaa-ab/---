A = list(map(int, input().split()))
min_i = 0
max_i = 0
i = 1
while i < len(A):
    if A[i] < A[min_i]:
        min_i = i
    if A[i] > A[max_i]:
        max_i = i
    i += 1

A[min_i], A[max_i] = A[max_i], A[min_i]
print(*A)