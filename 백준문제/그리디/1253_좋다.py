# 조합으로 2개씩 모두 뽑으면 최대 경우의 수는 1000 * 1999
# 조합과 딕셔너리를 이용해서, 모든 조합 경우의 수에서 더한 값이
# 딕셔너리에 키값으로 존재하면, 그 키 값이 가지는 수 만큼 답에 더했는데
# 이럴 경우, 자기 자신도 합해서 자기가 될 수도 있는 경우가 있었다.
# 예를 들어 0 + 3의 경우 3이되는데 3이 좋은 수가 되려면 다른 수 0, 3이어야 하지만
# 조합을 이용해서 구했을 때 그런 부분을 신경써줘야한다.
# 따라서 구현이 복잡해진다...

# 먼저 집합을 정렬한 후, 맨 뒤의 수 K부터 좋은 수인지 확인을 한다.
# 좋은 수 인지 확인을 할 때, 해당 K의 원소를 제외한 후의 리스트에서 확인을 하므로
# 위에서 문제된 부분을 해결할 수 있다.
# 두 수의 합이 K인지 확인을 하는 과정은, 맨 뒤의 원소와 맨 앞의 원소를 더하고
# 더한 값이 찾는 수보다 크면, 맨 뒤를 가리키던 인덱스를 한 칸 앞으로 옮김.
# 작으면, 맨 앞을 가리키던 인덱스를 한 칸 앞으로 당김.
# 이 과정을 거쳐서 찾게 되면, + 1을 하게 된다.
#
N = int(input())
# N은 최대 2000개
A = list(map(int, input().split()))
A.sort()
answer = 0
# A로 주어지는 수는 정수
for i in range(N):
    temp = A[:i] + A[i + 1:]
    start = 0
    end = len(temp) - 1
    while start < end:
        result = temp[start] + temp[end]
        # print(result, A[i])
        if result == A[i]:
            answer += 1
            break
        if result < A[i]:
            start += 1
        elif result > A[i]:
            end -= 1
print(answer)
