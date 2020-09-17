import sys
sys.stdin = open("원재의메모리복구하기.txt")

T = int(input())

for t in range(1, T+1):
    data = input()
    cnt = 0

    # 0에서 1로 바뀌거나 1에서 0으로 바뀌는 구간의 개수를 찾는다
    for i in range(len(data)-1):
        # 맨 처음이 1일 때
        if i == 0 and data[i] == '1':
            cnt += 1
        # 현재값이 0이고 다음값이 1일 때
        elif data[i] == '0' and data[i+1] == '1':
            cnt += 1
        # 현재값이 1이고 다음값이 0일 때
        elif data[i] == '1' and data[i+1] == '0':
            cnt += 1

    print("#{} {}".format(t, cnt))
