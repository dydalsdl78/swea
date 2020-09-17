import sys
sys.stdin = open("두개의숫자열.txt")

T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    if N < M:
        A, B = B, A
        N, M = M, N

    max_value = 0
    for i in range(N - M + 1):
        sum_value = 0
        for j in range(M):
            sum_value += A[i+j] * B[j]
        if max_value < sum_value:
            max_value = sum_value

    print("#{} {}".format(t, max_value))
