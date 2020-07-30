T = int(input())

for i in range(1, T+1):
    numbers = list(map(int, input().split()))
    mean = sum(numbers) / len(numbers)
    print(f"#{i} {round(mean)}")