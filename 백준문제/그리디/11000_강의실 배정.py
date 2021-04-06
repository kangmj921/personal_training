import sys

# 그냥 재귀와 배열의 원소를 하나하나 찾으면서 구현할 경우 시간초과....
# 최악의 경우 O(n!)의 시간복잡도 때문이다.
# 다른 방법을 이용하자.
def solution(lec):
    next_list = []
    last = 0
    for i, j in lec:
        if i >= last:
            last = j
        else:
            next_list.append([i, j])
    print(next_list)
    return next_list


N = int(input())
lecture_list = []
result = 0
for i in range(N):
    lecture_list.append(list(map(int, sys.stdin.readline().split())))
lecture_list.sort(key=lambda x: x[1])
a = lecture_list
while a:
    a = solution(a)
    result += 1
print(result)
