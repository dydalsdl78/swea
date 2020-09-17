import sys
sys.stdin = open("정곤이의단조증가하는수.txt")

# 잘봐두기!!!


def solve(ans):
    str_ans = str(ans)
    for i in range(len(str_ans)-1):
        if str_ans[i] > str_ans[i+1]:  # 한번이라도 앞에값이 뒤에 값보다 큰경우가 있다면
            return False               # 바로 False 반환
    return True                        # 모든 문자열 비교가 False에 걸리지 않으면 True 반환


T = int(input())

for t in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    max_value = -1

    for i in range(N-1):
        for j in range(i+1, N):
            ans = numbers[i] * numbers[j]
            if solve(ans) and ans > max_value:
                max_value = ans

    print("#{} {}".format(t, max_value))
