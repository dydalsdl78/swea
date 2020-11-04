T = int(input())

for t in range(1, T+1):
    N = int(input())
    arr = [list(input().split()) for _ in range(N)]

    ans = []
    for y in range(N):
        tmp = ""
        for x in range(N-1, -1, -1):
            tmp += arr[x][y]
        ans.append(tmp)

    for x in range(N-1, -1, -1):
        tmp = ""
        for y in range(N-1, -1, -1):
            tmp += arr[x][y]
        ans.append(tmp)

    for y in range(N-1, -1, -1):
        tmp = ""
        for x in range(N):
            tmp += arr[x][y]
        ans.append(tmp)

    print("#{}".format(t))
    for i in range(N):
        print("{}".format(' '.join(ans[i::N])))
