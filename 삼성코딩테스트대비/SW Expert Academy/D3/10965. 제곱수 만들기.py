# 시간초과.... 수를 걸러내거나 더 빨리 찾을 수 있는 범위를 찾거나 해야한다.
prime = [2]
for i in range(3, int(10000000 ** (0.5)), 2):
    for p in prime:
        if not i % p: break
    else:
        prime.append(i)
answer = []
T = int(input())
for tc in range(T):
    A = int(input())
    res = 1
    if A**0.5 != int(A**0.5):
        for p in prime:
            cnt = 0
            while not A % p:
                A //= p
                cnt += 1
            if cnt % 2:
                res *= p
            if A == 1 or p > A:
                break
        if A > 1:
            res *= A
    answer.append('#{} {}'.format(tc+1, res))
for ans in answer:
    print(ans)
