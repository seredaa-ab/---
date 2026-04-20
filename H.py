A = list(map(int, input().split()))
min_pos = 1001  # більше за максимальне можливе значення
for x in A:
    if 0 < x < min_pos:
        min_pos = x
print(min_pos)