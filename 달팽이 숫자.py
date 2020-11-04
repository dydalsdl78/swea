T = int(input())
visit = [[0]*N for _ in range(N)]


def check(x, y):
    if 0 <= x < N and 0 <= y < N:
        return True
    else:
        return False


for t in range(1, T+1):
    N = int(input())
    value = 1
    dir = 0
    x = [0, 1, 0, -1]
    y = [1, 0, -1, 0]
    for i in range(N):
        for j in range(N):
            for d in range(4):
                if check(x, y):
                    visit[i+x[d]][j+y[d]] = value
                    value += 1
                else:
                
