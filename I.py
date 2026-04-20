A = list(map(int, input().split()))
x = int(input())
closest = A[0]
min_diff = abs(A[0] - x)
for a in A:
    diff = abs(a - x)
    if diff < min_diff:
        min_diff = diff
        closest = a

print(closest)