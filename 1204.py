T = int(input())

for i in range(1, T+1):
    T_number = int(input())
    numbers = list(map(int, input().split()))
    
    max_value = numbers[0]
    max_cnt = numbers.count(numbers[0])
    
    for number in numbers:
        if numbers.count(number) >= max_cnt:
            max_cnt = numbers.count(number)
            max_value = number
        elif numbers.count(number) == max_cnt:
            if number > max_value:
                max_value = number

    print(f"#{i} {max_value}")
    
    
        