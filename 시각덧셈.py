import sys
sys.stdin = open("시각덧셈.txt")

T = int(input())

for t in range(1, T+1):
    time = list(map(int, input().split()))

    hour = time[0::2]
    minute = time[1::2]

    result_hour = sum(hour)
    result_min = sum(minute)
    if result_min >= 60:
        result_min -= 60
        result_hour += 1
    if result_hour >= 12:
        result_hour -= 12

    print("#{} {} {}".format(t, result_hour, result_min))
