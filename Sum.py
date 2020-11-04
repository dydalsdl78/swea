import sys
sys.stdin = open("Sum.txt")

T = 10

for t in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    max_value = 0

    # 행
    for x in range(100):
        sum_value = 0
        for y in range(100):
            sum_value += arr[x][y]
        if sum_value >= max_value:
            max_value = sum_value

    # 열
    for x in range(100):
        sum_value = 0
        for y in range(100):
            sum_value += arr[y][x]
        if sum_value >= max_value:
            max_value = sum_value

    # 왼쪽 대각선
    sum_value = 0
    for x in range(100):
        sum_value += arr[0+x][0+x]
    if sum_value >= max_value:
        max_value = sum_value

    # 오른쪽 대각선
    sum_value = 0
    for x in range(100):
        sum_value += arr[0+x][99-x]
    if sum_value >= max_value:
        max_value = sum_value

    print("#{} {}".format(N, max_value))
