T = int(input())

for i in range(1, T+1):
    numbers = list(map(int, input().split()))
    if numbers[0] > numbers[1]: 
        print(f"#{i} >")
    elif numbers[0] == numbers[1]: 
        print(f"#{i} =")
    elif numbers[0] < numbers[1]: 
        print(f"#{i} <")