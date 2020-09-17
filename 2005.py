import sys
sys.stdin = open("2005.txt")

T = int(input())

for t in range(1, T+1):
    N = int(input())
    arr = [[0] * (i+1) for i in range(N)]
    print("#{}".format(t))
    for i in range(N):
        for j in range(i+1):
            # 첫번째, 두번째줄
            if i == 0:
                arr[i][j] = 1
                print(arr[i][j])
            # # 두번째줄
            if i == 1:
                arr[i][j] = 1
                if i == j:
                    print(arr[i][j])
                else:
                    print(arr[i][j], end=" ")
            # 셋째줄 이후
            if i >= 2:
                # 맨 왼쪽
                if j == 0:
                    arr[i][j] = 1
                    print(arr[i][j], end=" ")
                # 가운데
                if 1 <= j <= i-1:
                    arr[i][j] = arr[i-1][j-1] + arr[i-1][j]
                    print(arr[i][j], end=" ")
                # 맨끝
                if j == i:
                    arr[i][j] = 1
                    print(arr[i][j])
