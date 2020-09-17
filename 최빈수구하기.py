import sys
sys.stdin = open("최빈수구하기.txt")

T = int(input())

for t in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))
    arr = [0] * 101

    for d in range(len(data)):
        arr[data[d]] += 1

    max_value = arr[0]
    for i in range(len(arr)):
        if arr[i] >= max_value:
            max_value = arr[i]
            result = i
    print("#{} {}".format(t, result))
