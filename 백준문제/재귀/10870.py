def pibonachi(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return pibonachi(n-1) + pibonachi(n-2)


N = int(input())
print(pibonachi(N))
