A = list(map(int, input().split()))
x = int(input())
i = 0
n = len(A)
while i < n and A[i] >= x:
    i += 1
print(i + 1)