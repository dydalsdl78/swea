import sys
sys.stdin = open("농작물수확하기.txt")

T = int(input())

for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    value = 0
    for i in range(N):
        if i == 0:
            start, end = N//2, N//2
            for j in range(start, end+1):
                value += arr[i][j]
            start -= 1
            end += 1

        if i != 0 and i < N//2:
            for j in range(start, end+1):
                value += arr[i][j]
            start -= 1
            end += 1

        if i != 0 and i >= N//2:
            for j in range(start, end+1):
                value += arr[i][j]
            start += 1
            end -= 1

    print("#{} {}".format(t, value))
