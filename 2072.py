T = int(input())

for i in range(1, T+1):
    sum_ls = 0
    numbers = list(map(int, input().split()))
    for number in numbers:
        if number % 2:
            sum_ls += number
    print(f"#{i} {sum_ls}")