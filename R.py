A = list(map(int, input().split()))
count = 0
i = 0
while i < len(A):
    j = i + 1
    while j < len(A):
        if A[i] == A[j]:
            count += 1
        j += 1
    i += 1

print(count)