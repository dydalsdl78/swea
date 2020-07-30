T = int(input())
numbers = []

for i in range(1, T+1):
    numbers = list(map(int, input().split()))
    max_value = numbers[0]
    for number in numbers:
        if number > max_value:
            max_value = number
    print(f"#{i} {max_value}")
