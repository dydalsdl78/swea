import sys
sys.stdin = open("1859.txt")

T = int(input())

for t in range(1, T+1):
    N = int(input())
    price = list(map(int, input().split()))

    cost = 0
    cnt = 0
    profit = 0
    start = 0
    result = 0
    for i in range(start, len(price)-1):
        cost += price[i]
        cnt += 1
        if price[i+1] * cnt > cost:
            sales = price[i+1] * cnt
            profit = sales - cost
            result += profit
        
    print("#{0} {1}".format(t, result))