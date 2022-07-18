# N의 범위가 최대 2 * 10 ^ 5 이므로, 시간복잡도가 O(nlogn)이나 O(N) 정도는 나와야 시간 제한에 걸리지 않을것이다.
# i번째 원소부터 j번째 원소까지의 합이 A, B에서 같은 쌍의 개수를 찾으려면
# 1 ~ N 까지의 수 중, 2개를 뽑는 경우의 수는, 최대 2 * 10 ^ 5 C 2 이므로,
# 찾는 경우의 수가 거의 N * N이다. 따라서 일일히 찾는 브루트포스 방식은 시간제한에 걸릴 것이다.
# 누적합을 어떻게 구하는지가 관건인데, 일반적으로 누적합을 구하는 알고리즘은 O(N)으로,
# i 번째에서 j 번째까지의 누적합 Sij 를, Sj(j번째 까지의 누적합) - Si - 1((i - 1)번째 까지의 누적합)으로 구할 수 있다.

# 두 A, B의 누적합이 같게 되면, 두 누적합의 차는 0이 될 것이다.
# A, B의 모든 원소를 돌면서, A[i] - B[i]의 리스트 C를 만든다. 그리고 C의 j번째 원소의 누적합은 곧
# A의 j번째 까지의 누적합 - B의 j번째 까지의 누적합과 같다. 따라서 이 누적합의 값을 0으로 만들어야 A와 B의 누적합이 같은 것이다.
# A와 B의 누적합을 같게 하는 i, j는 SCj = K일때, SCi = K이게 되는 i, j이다.
# 따라서 C 리스트의 누적합의 해당 값을 딕셔너리에 저장한다. 이때 딕셔너리에 저장되는 key 값은 누적합의 값이고, value는 해당 누적합이 나온 횟수이다.

# 만약 해당 값이 0 이라면, j번째 까지의 누적합이 같다는 뜻이다.
# 0이 아니라면, j보다 작은 i번째 까지의 누적합이 같은 값이 있다면, Aij = Bij 를 만족한다. i는 j 의 앞쪽 index 이므로, 이미 탐색이 다 되어있다.

# 따라서 Aij = Bij 인 것을 찾는데 O(N)의 시간복잡도로도 구할 수 있다.
answer = 0

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = [A[i] - B[i] for i in range(N)]
hash_table = {}
s = 0
for j in range(N):
    s += C[j]
    # s는 C의 누적합, 즉. A의 j번째 까지의 누적합 - B의 j 까지의 누적합임.
    if hash_table.get(s) is None:  # 딕셔너리에 누적합에 대해 저장된 횟수가 없음.
        hash_table[s] = 1  # 딕셔너리에 누적합 값을 key, 나온 횟수를 value 로 해서 저장.
        if not s:  # s가 0이면, A와 B의 j 까지의 누적합이 같다는 것.
            answer += 1
    else:  # 누적합의 값에 대해 이미 j보다 작은 i에서 나온적이 있음.
        if s:  # 만약 j 까지의 누적합의 값이 0이 아닌 값 K인 경우, Si = K 를 만족하는 i의 개수는 hash_table[s]와 같다.
            answer += hash_table[s]
            hash_table[s] += 1
            # 이때 i, j의 구간의 개수는, Si가 K인 것의 횟수이다.
            # 만약 Sj = 1, hash_table[1] = 2라면, j 까지의 누적합의 값이 1인데, 누적합의 값이 1을 만족하는 i가 2개라는 것이다.
            # 이 경우를 만족하는 i를 i1, i2 (i1 < i2)라 하면, 구간은 총 (i2, j), (i1, i2)로 나타낼 수 있다.
            # 따라서 answer 에 먼저 hash_table[s]를 더하고 j도 나중에 조건을 만족하는 i가 되므로, hash_table[s]에 1을 더한다.

        else:  # 만약 j 까지의 누적합의 값이 0인 경우, Si = 0 을 만족하는 i의 개수는 hash_table[s]와 같다.
            hash_table[s] += 1
            answer += hash_table[s]
            # 이때 i, j의 구간의 개수는, Sj가 0인 것을 포함해서 0이 나온 모든 구간의 개수이다.
            # 만약 Sj = 0, hash_table[s] = 2라면, j 까지의 누적합의 값이 0인데, 누적합의 값이 0을 만족하는 i가 2개라는 것이다.
            # 이 경우를 만족하는 i를 i1, i2 (i1 < i2)라 하면, 구간은 총 (i2, j), (i1, i2), (i1, j)로 나타낼 수 있다.
            # 따라서 먼저 hash_table[s]에 1을 더한 후, answer 에 더한다.
print(answer)
