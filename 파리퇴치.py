T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_value = 0

    for i in range(N-M+1):
        for j in range(N-M+1):
            sum_value = 0
            for x in range(M):
                for y in range(M):
                    sum_value += arr[i+x][j+y]
            if sum_value >= max_value:
                max_value = sum_value

    print("#{} {}".format(t, max_value))
