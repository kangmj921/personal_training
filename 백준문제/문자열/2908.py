A, B = input().split()
list_a = list(A)
list_b = list(B)
list_a.reverse()
list_b.reverse()
a = int("".join(list_a))
b = int("".join(list_b))
print(max(a,b))