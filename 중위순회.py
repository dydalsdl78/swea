def tree(node):
    if node:
        tree(arr[node][1])
        print(arr[node][3], end='')
        tree(arr[node][2])


T = 10

for t in range(1, T+1):
    N = int(input())
    arr = [[0] * 4 for _ in range(N+1)]

    for n in range(1, N+1):
        tmp = list(input().split())
        if len(tmp) == 4:
            arr[n][0], arr[n][1], arr[n][2], arr[n][3] = int(
                tmp[0]), int(tmp[2]), int(tmp[3]), tmp[1]
        elif len(tmp) == 3:
            arr[n][0], arr[n][1], arr[n][3] = int(tmp[0]), int(tmp[2]), tmp[1]
        else:
            arr[n][0], arr[n][3] = int(tmp[0]), tmp[1]

    print("#{}".format(t), end=' ')
    tree(1)
    print()
