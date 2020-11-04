# bfs로 풀기!
import sys
sys.stdin = open('미로2.txt')


def bfs(x, y):
    global flag
    flag = 0
    # 빈 큐 생성
    q = []
    # 방문 행렬
    visit = [[0] * 100 for _ in range(100)]
    # 인큐
    q.append([s_x, s_y])
    # 방문처리
    visit[s_x][s_y] = 1

    d_x = [0, 0, -1, 1]
    d_y = [-1, 1, 0, 0]

    # q가 비어있지 않을 때
    while q:
        # 디큐
        n_p = q.pop(0)
        for d in range(4):
            if visit[n_p[0]+d_x[d]][n_p[1]+d_y[d]] == 0 and maze[n_p[0]+d_x[d]][n_p[1]+d_y[d]] == 0:
                q.append([n_p[0]+d_x[d], n_p[1]+d_y[d]])
                visit[n_p[0]+d_x[d]][n_p[1]+d_y[d]] = 1
            elif visit[n_p[0]+d_x[d]][n_p[1]+d_y[d]] == 0 and maze[n_p[0]+d_x[d]][n_p[1]+d_y[d]] == 3:
                flag = 1
                return 0


def findStart(maze):
    for i in range(100):
        for j in range(100):
            if maze[i][j] == 2:
                return i, j


T = 10

for t in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(100)]
    s_x, s_y = findStart(maze)
    bfs(s_x, s_y)

    print('#{} {}'.format(t, flag))
