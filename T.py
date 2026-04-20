A = list(map(int, input().split()))
count = 0
i = 0
while i < len(A):
    j = 0
    found = False

    while j < i:
        if A[i] == A[j]:
            found = True
        j += 1
    if not found:
        count += 1
    i += 1
print(count)