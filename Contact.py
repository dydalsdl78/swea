
def bfs(v):
    q = []
    # 인큐
    q.append(v)
    visit[v] = 1
    while q:
        # 디큐
        v = q.pop(0)
        for w in range(1, 101):
            if arr[v][w] and visit[w] == 0:
                q.append(w)
                visit[w] = visit[v] + 1


T = 10

for t in range(1, T + 1):
    N, s = map(int, input().split())
    arr = [[0] * 101 for _ in range(101)]
    tmp = list(map(int, input().split()))
    for i in range(1, N//2 + 1):
        arr[tmp[2 * (i-1)]][tmp[2 * (i-1) + 1]] = 1

    visit = [0] * 101

    bfs(s)

    maxIdx = 0
    maxV = 0
    for j in range(len(visit)):
        if j > maxIdx and visit[j] >= maxV:
            maxV = visit[j]
            maxIdx = j
    print("#{} {}".format(t, maxIdx))
