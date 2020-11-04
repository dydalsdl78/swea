T = int(input())

for t in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    # 최대값을 찾고 그 이전에는 전부 산 후에 최대값에서 판다.
    # 최대값 이후의 구간에서 다시 최대값을 찾고 그 이전에서 사고 최대값에서 판다.
    # 반복
    s = 0
    for i in arr:
        s = i
        for s in
