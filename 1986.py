import sys
sys.stdin = open("1986.txt")

T = int(input())

for t in range(1, T+1):
    N = int(input())
    result = 0
    for i in range(1, N+1):
        if i % 2:
            result += i
        else:
            result -= i
    print("#{} {}".format(t, result))
