A = list(map(int, input().split()))
max_val = A[0]
index = 0
for i in range(1, len(A)):
    if A[i] > max_val:
        max_val = A[i]
        index = i
print(max_val, index)