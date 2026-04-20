A = list(map(int, input().split()))
B = []
i = 0
while i < len(A):
    if i + 1 < len(A):
        B.append(A[i + 1])
        B.append(A[i])
    else:
        B.append(A[i])
    i += 2
print(*B)