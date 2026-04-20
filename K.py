A = list(map(int, input().split()))
count = 1
i = 1
while i < len(A):
    if A[i] != A[i - 1]:
        count += 1
    i += 1
print(count)