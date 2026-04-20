A = list(map(int, input().split()))
i = 0
while i < len(A):
    x = A[i]
    count = 0
    j = 0
    while j < len(A):
        if A[j] == x:
            count += 1
        j += 1
    if count == 1:
        print(x, end=' ')
    i += 1
