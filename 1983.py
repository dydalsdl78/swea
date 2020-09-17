import sys
sys.stdin = open("1983.txt")

T = int(input())

for t in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    grade_ls = []
    for i in range(len(arr)):
        value = arr[i][0] * 0.35 + arr[i][1] * 0.45 + arr[i][2] * 0.2
        grade_ls.append(value)

    for i in range(len(grade_ls)):
        for j in range(len(grade_ls)-i-1):
            if grade_ls[j] < grade_ls[j+1]:
                grade_ls[j], grade_ls[j+1] = grade_ls[j+1], grade_ls[j]

    grade = ["A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"]

    for g, v in zip(grade, grade_ls):
        for d in range(0, len(grade_ls), N/10):
            grade_ls
