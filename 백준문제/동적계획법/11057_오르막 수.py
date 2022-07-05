# N 을 입력받고 N 자리의 오르막 수의 개수를 구한다.
# dp 리스트를 N + 1 * N + 1 크기의 2차원으로 선언한다.
# dp[i][j]의 값은, j번째 자리수가 i일때 가지는 오르막 수의 값이다.
# 예를 들어, N이 1일때 dp의 값은,
# 0 1
# 0 1
# 0 1
# ...
# 0 1로 나타낼 수 있다.
# N이 2 이상일땐, 앞자리에 어떤 수가 오느냐에따라 오르막 수의 값이 결정된다.
# N이 2일때....    N이 3일때...
# 0 0~9 10개      0 0 0~9 10개
# 1 1~9 9개       0 1 1~9 9개
# ...55개         0 2 2~9 8개
#                 ... 55개
#                 1 1 1~9 9개
#                 1 2 2~9 8개
#                 ...45개
# 따라서 첫 자리가 어떤 수로 시작하느냐에 따라 오르막 수의 개수를 dp를 이용해 구할 수 있다.
# 0으로 시작할 경우, N 자리의 오르막 수의 값은 N - 1 자리의 모든 오르막 수의 값과 같다.
# 1로 시작할 경우, N 자리의 오르막 수의 값은, N - 1 자리의 모든 오르막 수 - (0 으로 시작하는 N - 1 자리수의 오르막 수)
# 따라서, 시작하는 수가 i(0~9) 일때, N 자리의 오르막 수의 값은
# N - 1 자리수의 모든 오르막 수 - (i - 1 까지 시작하는 N - 1 자리의 오르막 수의 합)으로 나타낼 수 있으며
# 최종적으로 답은 dp_list[0~9][N]로 구할 수 있다.

N = int(input())
dp_list = [[0] * (N + 1) for _ in range(11)]
answer = 0
for i in range(1, 11):
    dp_list[i][1] = 1  # N이 1일때에 대하여 dp 값 초기화
for i in range(2, N + 1):  # N이 2 이상일땐, 앞자리의 수에 따라 오르막 수의 개수가 결정된다.
    temp = sum(dp_list[k][i - 1] for k in range(1, 11))  #
    dp_list[1][i] = temp
    for j in range(2, 11):
        temp -= dp_list[j - 1][i - 1]
        dp_list[j][i] = temp
for i in range(1, 11):
    answer += dp_list[i][N]
print(answer % 10007)
